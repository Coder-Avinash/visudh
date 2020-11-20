from django import forms
from .models import StudentForm

class StudentForm(forms.ModelForm):
    class Meta:
        # firstname = forms.CharField(label="Enter first name",max_length=50)
        # lastname  = forms.CharField(label="Enter last name", max_length = 100)
        model= StudentForm
        fields= ["firstname", "lastname"]
