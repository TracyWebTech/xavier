# -*- coding: utf-8 -*-

from django.views import generic

from schools.models import School


class HomePageView(generic.TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        #context[''] = 
        return context


class GenericTemplateMixin(object):
    base_template = None

    def get_context_data(self, **kwargs):
        meta = self.model._meta
        context = super(GenericTemplateMixin, self).get_context_data(**kwargs)
        context.update({
            'base_template': self.base_template,
            'verbose_name': meta.verbose_name,
            'verbose_name_plural': meta.verbose_name,
        })
        return context

    def get_template_names(self):
        names = super(GenericTemplateMixin, self).get_template_names()
        names.append('generic/object%s.html' % self.template_name_suffix)
        return names


class ListView(GenericTemplateMixin, generic.ListView):
    paginate_by = 20


class DetailView(GenericTemplateMixin, generic.DetailView):
    pass


class CreateView(GenericTemplateMixin, generic.CreateView):
    pass


class UpdateView(GenericTemplateMixin, generic.UpdateView):
    pass


class DeleteView(GenericTemplateMixin, generic.DeleteView):
    pass
