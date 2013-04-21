# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy

from xavier import views
from classes import models


class_list = views.ListView.as_view(model=models.Class)
class_detail = views.DetailView.as_view(model=models.Class)
class_create = views.CreateView.as_view(model=models.Class)
class_update = views.UpdateView.as_view(model=models.Class)
class_delete = views.DeleteView.as_view(model=models.Class)
