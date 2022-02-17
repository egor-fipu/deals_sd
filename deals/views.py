from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Deal, TopCustomer
from .serializers import FileSerializer, TopCustomerSerializer
from .services import get_data


class DealsAPIView(APIView):

    def post(self, request):
        serializer = FileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            deal_obj_list, tc_obj_list = get_data(
                serializer.validated_data['deals']
            )
            Deal.objects.bulk_create(deal_obj_list)
            TopCustomer.objects.all().delete()
            TopCustomer.objects.bulk_create(tc_obj_list)
        except Exception as error:
            message = {
                'Status': 'Error',
                'Desc': f'{error}- в процессе обработки файла произошла ошибка'
            }
            return Response(data=message, status=status.HTTP_400_BAD_REQUEST)

        message = {'Status': 'OK - файл был обработан без ошибок'}
        return Response(data=message, status=status.HTTP_200_OK)

    def get(self, request):
        queryset = TopCustomer.objects.all()
        serializer = TopCustomerSerializer(queryset, many=True)
        data = {'response': serializer.data}
        return Response(data=data, status=status.HTTP_200_OK)
