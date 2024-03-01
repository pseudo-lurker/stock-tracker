from datetime import datetime
from pytz import timezone
from time import time

from django.conf import settings

from .models import PriceChangeEvent

MULTIPLIER = 1
TIMESPAN = 'hour'
SORTING = 'asc'
LIMIT = 50000  # Max allowed limit, not actually reached.
DAYS_365 = 31536000000  # In milliseconds as required by api
HOURS_30 = 108000000  # In milliseconds as required by api


def check_price_changes(agg, company):
    last_price = float(company.last_price)
    flat_change = round(agg.open - last_price,  2)
    percentage_change = round(agg.open / last_price * 100 - 100, 2)

    if settings.PRICE_CHANGE_TYPE == 'flat':
        change = abs(flat_change)
    elif settings.PRICE_CHANGE_TYPE == 'percentage':
        change = abs(percentage_change)
    else:
        raise ValueError('Invalid `PRICE_CHANGE_TYPE` in settings!')

    if change > float(settings.PRICE_CHANGE_FACTOR):
        change_time = datetime.fromtimestamp(
            agg.timestamp / 1000, tz=timezone(settings.TIME_ZONE)
        )

        # Ignores duplicates due to time overlap.
        PriceChangeEvent.objects.get_or_create(
            company=company,
            before_price=company.last_price,
            after_price=agg.open,
            flat_change=flat_change,
            percentage_change=percentage_change,
            changed=change_time
        )

        company.last_price = agg.open
        company.save()


def check_company_prices(client, company, historic=False):
    to_time = int(time() * 1000)  # Converting to milliseconds as required
    if historic:
        from_time = to_time - DAYS_365
    else:
        # Running 30 hours in the past to reliably get data.
        from_time = to_time - HOURS_30

    hourly_aggregates = client.get_aggs(
        ticker=company.ticker,
        multiplier=MULTIPLIER,
        timespan=TIMESPAN,
        from_=from_time,
        to=to_time,
        sort=SORTING,
        limit=LIMIT
    )

    if not company.last_price:
        company.last_price = hourly_aggregates[0].open
        company.save()

    for agg in hourly_aggregates:
        check_price_changes(agg, company)
