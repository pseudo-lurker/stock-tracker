from rest_framework import serializers

from .models import Company, PriceChangeEvent


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class PriceChangeEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceChangeEvent
        fields = '__all__'

    company = CompanySerializer()
