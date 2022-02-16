import csv
from io import TextIOWrapper

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Deal, TopCustomer
from .serializers import FileSerializer, TopCustomerSerializer
from .services import top_customers


class DealsAPIView(APIView):

    def post(self, request):
        serializer = FileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            csvfile = TextIOWrapper(
                serializer.validated_data['deals'], encoding='utf8'
            )
            reader = csv.DictReader(csvfile)
            deal_obj_list = []
            customers = {}
            for row in reader:
                deal_obj_list.append(Deal(**row))

                if row['customer'] not in customers:
                    customers[row['customer']] = {
                        'spent_money': float(row['total']),
                        'gems': {row['item']},
                        'select': set()
                    }
                else:
                    customers[row['customer']]['spent_money'] += float(row['total'])
                    customers[row['customer']]['gems'].add(row['item'])

            Deal.objects.bulk_create(deal_obj_list)

            tc_obj_list = top_customers(customers)
            TopCustomer.objects.all().delete()
            TopCustomer.objects.bulk_create(tc_obj_list)
        except Exception as error:
            message = {
                'Status': 'Error',
                'Desc': f'{error} - в процессе обработки файла произошла ошибка'
            }
            return Response(data=message, status=status.HTTP_400_BAD_REQUEST)

        message = {'Status': 'OK - файл был обработан без ошибок'}
        return Response(data=message, status=status.HTTP_200_OK)

    def get(self, request):
        queryset = TopCustomer.objects.all()
        serializer = TopCustomerSerializer(queryset, many=True)
        data = {
            'response': serializer.data
        }
        return Response(data=data, status=status.HTTP_200_OK)
