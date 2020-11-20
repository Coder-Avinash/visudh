from django.db import models

class resgitration(models.Model):
    firstname = models.CharField(max_length= 50)
    lastname = models.CharField(max_length= 50)
    username = models.CharField(max_length= 50)
    email = models.EmailField(max_length= 50)
    mobile = models.PositiveIntegerField(primary_key= True)
