from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Student, Employee


class UserCreateForm(UserCreationForm):
    class Meta:
        model = get_user_model()

    def clean_username(self):
        username = self.cleaned_data["username"]
        UserModel = get_user_model()
        try:
            UserModel._default_manager.get(username=username)
        except UserModel.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


class UserChangingForm(UserChangeForm):
    class Meta:
        model = get_user_model()


class StudentRegistrationForm(UserCreateForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'username', 'birthday', 'gender')
        exclude = ('is_staff', 'date_joined', 'last_login')


class EmployeeRegistrationForm(UserCreateForm):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'username')
        exclude = ('is_staff', 'date_joined', 'last_login',)
