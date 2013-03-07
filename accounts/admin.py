# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _
from .forms import StudentRegistrationForm, EmployeeRegistrationForm
from .forms import UserCreateForm, UserChangingForm
from .models import User, Student, Teacher, Employee


class UserAdmin(DjangoUserAdmin):
    # add fields here to appear when registering user.
    add_form = UserCreateForm
    form = UserChangingForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'password1',
                       'password2', 'email', 'birthday', 'gender', 'groups',
                       'user_permissions')}),
    )

    # add fields here to appear when changing user
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_(u'Personal info'), {'fields': ('first_name', 'last_name', 'email',
                              'birthday', 'gender')}),
        (_(u'Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_(u'Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


class StudentAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('code', 'first_name', 'last_name', 'username',
                       'password1', 'password2', 'email', 'birthday', 'gender',
                       'user_permissions')}),
    )


class EmployeeAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'password1',
                       'password2', 'email', 'birthday', 'gender', 'groups',
                       'user_permissions')}),
    )


class TeacherAdmin(EmployeeAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'password1',
                       'password2', 'email', 'birthday', 'gender',
                       'user_permissions')}),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Employee, EmployeeAdmin)
