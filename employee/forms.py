from django import forms
from .models import Employee_Profile
from django.contrib.auth.models import User


# class EmployeeForm(forms.ModelForm):
#     class Meta:
#         model = Employee
#         fields = "__all__"
#
#
# class LoginForm(forms.Form):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = Employee_Profile
        fields = "__all__"

class EmployeeForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_repeat = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
