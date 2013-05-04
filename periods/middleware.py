
from . import get_subperiod, set_subperiod

from django.utils.functional import SimpleLazyObject


class XavierPeriodMiddleware(object):

    def process_request(self, request):
        request.subperiod = SimpleLazyObject(lambda: get_subperiod(request))
        request.set_subperiod = lambda subperiod: \
                                            set_subperiod(request, subperiod)
