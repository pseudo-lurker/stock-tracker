from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet

from .models import PriceChangeEvent
from .serializers import PriceChangeEventSerializer


class PriceChangeViewSet(ListAPIView, GenericViewSet):
    queryset = PriceChangeEvent.objects.all().order_by('-id')
    serializer_class = PriceChangeEventSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = {
        'before_price': ['exact', 'lte', 'gte'],
        'after_price': ['exact', 'lte', 'gte'],
        'flat_change': ['exact', 'lte', 'gte'],
        'percentage_change': ['exact', 'lte', 'gte'],
        'changed': ['exact'],
        'company__name': ['exact'],
        'company__ticker': ['exact']
    }
    search_fields = [
        'before_price',
        'after_price',
        'changed',
        'flat_change',
        'percentage_change',
        'company__name',
        'company__ticker'
    ]
    permission_classes = [AllowAny]
