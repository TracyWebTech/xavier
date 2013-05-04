
from .models import Period

from django.utils import timezone
from django.utils.functional import SimpleLazyObject


def get_subperiod(request):
    subperiod = request.session.get('subperiod')

    if not subperiod:
        year = timezone.now().year
        try:
            period = Period.objects.get(year=timezone.now().year)
        except Period.DoesNotExist:
            return None

        subperiod = period.get_current_subperiod()

    return subperiod


class XavierPeriodMiddleware(object):

    def process_request(self, request):
        request.subperiod = SimpleLazyObject(lambda: get_subperiod(request))
