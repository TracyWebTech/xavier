# -*- coding: utf-8 -*-

from xavier import views
from accounts import models
from schools.models import School


class AccountBaseMixin(object):

    @property
    def current_school(self):
        return School.objects.get_current(self.request)

    def get_queryset(self):
        queryset = super(AccountBaseMixin, self).get_queryset()
        return queryset.filter(school=self.current_school)


class AccountList(AccountBaseMixin, views.ListView):
    paginate_by = 20


class AccountDetail(AccountBaseMixin, views.DetailView):
    pass


class AccountCreate(AccountBaseMixin, views.CreateView):
    pass


class AccountUpdate(AccountBaseMixin, views.UpdateView):
    pass


class AccountDelete(AccountBaseMixin, views.DeleteView):
    success_url = '../../'


# Students
student_list = AccountList.as_view(model=models.Student)
student_detail = AccountDetail.as_view(model=models.Student)
student_create = AccountCreate.as_view(model=models.Student)
student_update = AccountUpdate.as_view(model=models.Student)
student_delete = AccountDelete.as_view(model=models.Student)

# Employees
employee_list = AccountList.as_view(model=models.Employee)
employee_detail = AccountDetail.as_view(model=models.Employee)
employee_create = AccountCreate.as_view(model=models.Employee)
employee_update = AccountUpdate.as_view(model=models.Employee)
employee_delete = AccountDelete.as_view(model=models.Employee)

# Teachers
teacher_list = AccountList.as_view(model=models.Teacher)
teacher_detail = AccountDetail.as_view(model=models.Teacher)
teacher_create = AccountCreate.as_view(model=models.Teacher)
teacher_update = AccountUpdate.as_view(model=models.Teacher)
teacher_delete = AccountDelete.as_view(model=models.Teacher)
