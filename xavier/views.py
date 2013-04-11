# -*- coding: utf-8 -*-

from django.views import generic
from towel import modelview

from schools.models import School


class HomePageView(generic.TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        #context[''] = 
        return context


class ModelView(modelview.ModelView):
    def get_current_school(self, request):
        # School's manager already performs a cache for the
        # ``get_current`` method so you don't need worry about that
        return School.objects.get_current(request)
