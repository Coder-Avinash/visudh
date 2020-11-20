from .views import GeneratePdf
from django.urls import path


urlpatterns = [


    #we have defined a  url pdf/
    #and whenever the user will request this url pdf<strong>,</strong>check the file urls.py inside app HTMLtoPDF.

    path('', GeneratePdf.as_view()),
]
