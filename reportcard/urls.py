
from django.views.generic import TemplateView                                    

from django.conf.urls import include, patterns, url                              

urlpatterns = patterns('',                                                       
    url(r'^$', TemplateView.as_view(template_name='reportcard/report-card.html')),
)
