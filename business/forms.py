from django import forms
from .models import User, Business_Profile


class BusinessProfileForm(forms.ModelForm):
    class Meta:
        model = Business_Profile
        fields = "__all__"

class BusinessForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_repeat = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
