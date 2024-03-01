from django.apps import apps
from django.conf import settings
from django.core.management.base import BaseCommand
from polygon import RESTClient

from ...utils import check_company_prices


class Command(BaseCommand):
    help = 'Fill initial historic data.'

    def handle(self, *args, **options):
        client = RESTClient(api_key=settings.POLYGON_API_KEY)
        company_model = apps.get_model('app', 'Company')

        for company in company_model.objects.all():
            check_company_prices(client, company, True)
