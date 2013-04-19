# -*- coding: utf-8 -*-

from xavier import views
from accounts import models


# Students
student_list = views.List.as_view(model=models.Student)
student_detail = views.Detail.as_view(model=models.Student)
student_create = views.Create.as_view(model=models.Student)
student_update = views.Update.as_view(model=models.Student)
student_delete = views.Delete.as_view(model=models.Student)

# Employees
employee_list = views.List.as_view(model=models.Employee)
employee_detail = views.Detail.as_view(model=models.Employee)
employee_create = views.Create.as_view(model=models.Employee)
employee_update = views.Update.as_view(model=models.Employee)
employee_delete = views.Delete.as_view(model=models.Employee)

# Teachers
teacher_list = views.List.as_view(model=models.Teacher)
teacher_detail = views.Detail.as_view(model=models.Teacher)
teacher_create = views.Create.as_view(model=models.Teacher)
teacher_update = views.Update.as_view(model=models.Teacher)
teacher_delete = views.Delete.as_view(model=models.Teacher)
