from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponse
from customer.models import Customer_Profile
from employee.models import Employee_Profile
from business.models import Business_Profile
from django.contrib.auth.decorators import login_required
#pdf libraries
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape, A4




@login_required(login_url='/customer/login')
def cust_search(request):
     return render(request, 'card/customer_search.html')



@login_required(login_url='/employee/login')
def emp_search(request):
     return render(request, 'card/employee_search.html')

@login_required(login_url='/business/login')
def busi_search(request):
     return render(request, 'card/business_search.html')


@login_required(login_url='/customer/login')
def results(request):

    if 'q' in request.GET and request.GET['q']:
        q=request.GET['q']
        all_username = User.objects.filter(username=q)
        for i in all_username:
            id=i.id

        all_details = Customer_Profile.objects.filter(user_id=id) or Employee_Profile.objects.filter(user_id=id) or Business_Profile.objects.filter(user_id=id)
        for j in all_details:
            if j.registered_as == "CUS":
                return render(request, 'card/customercard.html',{'all_username':all_username, 'all_details':all_details})
            elif j.registered_as == "EMP":
                return render(request, 'card/employeecard.html',{'all_username':all_username, 'all_details':all_details})
            elif j.registered_as == "BUSI":
                return render(request, 'card/businesscard.html',{'all_username':all_username, 'all_details':all_details})
            else:
                s="NO CARD FOUND"
                return HttpResponse(s)

#pdf Function
def generate_pdf(request):
    response = HttpResponse(content_type= 'application/pdf')
    # d= datetime.today().strftime('%Y-%m-%d')
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)

    #data to Print
    p.drawString(250, 800, "VISUDH AJIVAM")
    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response
