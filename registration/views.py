from django.shortcuts import render
from .forms import StudentForm

def index(request):
    student = StudentForm(request.POST or None)
    if student.is_valid():
        student.save()
    return render(request,"registration/index.html",{'form':student})
