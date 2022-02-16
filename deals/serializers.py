from rest_framework import serializers

from .models import TopCustomer


class FileSerializer(serializers.Serializer):
    deals = serializers.FileField(required=True)

    def validate_deals(self, value):
        if '.csv' not in value.name:
            raise serializers.ValidationError(
                'Файл должен иметь расширение ".csv"'
            )
        return value


class TopCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopCustomer
        fields = ('username', 'spent_money', 'gems')
