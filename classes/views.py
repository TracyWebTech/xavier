# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy

from xavier import views
from classes import models


class_list = views.List.as_view(model=models.Class)
class_detail = views.Detail.as_view(model=models.Class)
class_create = views.Create.as_view(model=models.Class)
class_update = views.Update.as_view(model=models.Class)
class_delete = views.Delete.as_view(model=models.Class)
