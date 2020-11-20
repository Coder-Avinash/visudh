from django import forms
from .models import User, Customer_Profile


# class CustomerForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = "__all__"


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer_Profile
        fields = "__all__"

class CustomerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_repeat = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
