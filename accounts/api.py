from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource

from accounts import models


class StudentResource(ModelResource):
    class Meta:
        queryset = models.Student.on_school.all()
        allowed_methods = ['get']
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()
