from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    username = models.CharField(max_length = 20)
    email = models.EmailField()
    password = models.CharField(max_length = 20)
    password_repeat = models.CharField(max_length = 20)
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    phone_number = models.CharField(max_length = 10)


class Employee_Profile(models.Model):
    user = models.OneToOneField(User, blank=True, on_delete=models.CASCADE)

    Gender_Choice=(
    (u'M', u'Male'),
    (u'F', u'Female'),
    (u'O', u'Other'),
    )

    Maritial_Status=(
    (u'M', u'Married'),
    (u'U', u'Unmarried'),
    )

    Blood_Groups=(
    (u'A+', u'A+'),
    (u'A-', u'A-'),
    (u'B+', u'B+'),
    (u'B-', u'B-'),
    (u'O+', u'O+'),
    (u'O-', u'O-'),
    (u'AB+', u'AB+'),
    (u'AB-', u'AB-'),
    )

    Qualification_Details=(
    (u'10', u'10'),
    (u'12', u'12'),
    (u'UG', u'UG'),
    (u'PG', u'PG'),
    )

    Registered_As=(
    (u'EMP', u'Employee'),
    )

    registered_as= models.CharField(max_length=3, default="EMP", choices=Registered_As)
    gender = models.CharField(max_length=2, choices=Gender_Choice)
    dob = models.DateField(max_length=8)
    aadhar_number = models.CharField(max_length=12, blank=True)
    pan_number = models.CharField(max_length=10, blank=True)
    phone_number = models.CharField(max_length = 10)
    qualifications = models.CharField(max_length=2, choices=Qualification_Details)
    documents = models.FileField(upload_to='qualification_documents', blank=True)
    job_experience = models.CharField(max_length=20)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    state = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=3, choices=Blood_Groups)
    number_of_family_members = models.CharField(max_length=2)
    alt_phone_number = models.CharField(max_length=10, blank=True)
    disease = models.CharField(max_length=20, default="NO", blank=True)
    maritial_status = models.CharField(max_length=2, choices=Maritial_Status)
    refrence_record = models.CharField(max_length=30, blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    profile_status = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
