
from .models import Period

def periods(request):
    return {
        'subperiod_selected': request.subperiod,
        'all_periods': Period.objects.all(),
    }
