
from django.utils import timezone


def set_subperiod(request, subperiod):
    request.session['subperiod'] = subperiod


def get_subperiod(request):
    from .models import Period

    subperiod = request.session.get('subperiod')

    if not subperiod:
        year = timezone.now().year
        try:
            period = Period.objects.get(year=timezone.now().year)
        except Period.DoesNotExist:
            return None

        subperiod = period.get_current_subperiod()

    return subperiod
