
from .models import Period, SubPeriod

def periods(request):
    periods = {}
    for period in Period.objects.all():
        periods[period] = SubPeriod.objects.filter(period_id=period.id)

    return {
        'subperiod_selected': request.subperiod,
        'all_period': periods,
    }
