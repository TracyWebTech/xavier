from tastypie import fields
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource

from attendances import models


class AttendanceBookResource(ModelResource):
    class Meta:
        queryset = models.AttendanceBook.on_school.all()
        allowed_methods = ['get']
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()


class AttendanceResource(ModelResource):
    attendance_book = fields.ForeignKey(
        'attendances.api.AttendanceBookResource',
        attribute='attendance_book',
        related_name='attendances',
    )
    student = fields.ForeignKey(
        'accounts.api.StudentResource',
        attribute='student',
        related_name='attendances',
    )

    class Meta:
        queryset = models.Attendance.on_school.all()
        allowed_methods = ['create', 'update']
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()
