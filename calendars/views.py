from django.views import generic
from django.utils.translation import ugettext


class Calendar(generic.TemplateView):
    template_name = 'calendars/calendar.html'

    def get_context_data(self, **kwargs):
        context = super(Calendar, self).get_context_data(**kwargs)
        context.update({
            'title': ugettext('Calendar'),
        })
        return context
