from django.db import models

class StudentForm(models.Model):
    firstname = models.CharField(max_length= 50)
    lastname = models.CharField(max_length= 50)
