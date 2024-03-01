import os

from celery import Celery
from polygon import RESTClient
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tracker.settings")
app = Celery("tracker")
app.config_from_object("django.conf:settings", namespace="CELERY")


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(
        settings.CHECK_PERIOD, check_stock_prices.s(), name='add every 10'
    )


@app.task
def check_stock_prices():
    # Imported here to allow for the app to be loaded
    from app.models import Company
    from app.utils import check_company_prices

    print("This is a periodic task to check prices.")
    client = RESTClient(api_key=settings.POLYGON_API_KEY)

    for company in Company.objects.all():
        check_company_prices(client, company, True)

