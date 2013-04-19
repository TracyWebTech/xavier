# -*- coding: utf-8 -*-

from xavier import views
from accounts import models


# Students
student_list = views.ListView.as_view(model=models.Student)
student_detail = views.DetailView.as_view(model=models.Student)
student_create = views.CreateView.as_view(model=models.Student)
student_update = views.UpdateView.as_view(model=models.Student)
student_delete = views.DeleteView.as_view(model=models.Student)

# Employees
employee_list = views.ListView.as_view(model=models.Employee)
employee_detail = views.DetailView.as_view(model=models.Employee)
employee_create = views.CreateView.as_view(model=models.Employee)
employee_update = views.UpdateView.as_view(model=models.Employee)
employee_delete = views.DeleteView.as_view(model=models.Employee)

# Teachers
teacher_list = views.ListView.as_view(model=models.Teacher)
teacher_detail = views.DetailView.as_view(model=models.Teacher)
teacher_create = views.CreateView.as_view(model=models.Teacher)
teacher_update = views.UpdateView.as_view(model=models.Teacher)
teacher_delete = views.DeleteView.as_view(model=models.Teacher)
