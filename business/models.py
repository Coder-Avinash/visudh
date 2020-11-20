from django.db import models
from django.contrib.auth.models import User

class Business_Profile(models.Model):
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

    Registered_As=(
    (u'BUSI', u'Business'),
    )

    Business_Catogry=(
    (u'MDR', u'MEDICINE RETAIL'),
    (u'MDW', u'MEDICINE WHOLESALE'),
    (u'MDD', u'MEDICINE DISTRIBUTOR'),
    (u'LND', u'LABS AND DIAGNOSTIC'),
    (u'HSP', u'HOSPITAL'),
    (u'NH', u'NURSING HOME'),
    (u'CLNC', u'CLINIC'),
    (u'DOC', u'DOCTOR'),
    (u'PTPY', u'PHYSIOTHERAPY'),

    )

    registered_as= models.CharField(max_length=4, default="BUSI", choices=Registered_As)
    gender = models.CharField(max_length=2, choices=Gender_Choice)
    dob = models.DateField(max_length=8)
    aadhar_number = models.CharField(max_length=12, blank=True)
    phone_number = models.CharField(max_length = 10)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50, blank=True)
    maritial_status = models.CharField(max_length=2, choices=Maritial_Status)
    husband_wife_name = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=100)
    business_address = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    state = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    business_phone_number = models.CharField(max_length=10)
    refrence_record = models.CharField(max_length=30, blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    business_picture = models.ImageField(upload_to='business_profile_images', blank=True)
    business_category = models.CharField(max_length=4, choices=Business_Catogry)
    business_registration_number = models.CharField(max_length=20)
    business_license = models.CharField(max_length=20)
    business_gst_number =  models.CharField(max_length=15)
    documents_upload = models.FileField(upload_to='business_documents', blank=True)

    profile_status = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
