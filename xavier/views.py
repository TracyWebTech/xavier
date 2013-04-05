# -*- coding: utf-8 -*-

from django.views import generic


class HomePageView(generic.TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        #context[''] = 
        return context
