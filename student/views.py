from django.shortcuts import render,redirect
from .models import StudentDetails

# Create your views here.

def NewPage(request):
    na = request.POST.get("name1")
    fna = request.POST.get("name2")
    mail = request.POST.get("mail1")
    Qua = request.POST.get("Q1")
    address = request.POST.get("address1")
    ph = request.POST.get("ph1")

    o_ref = StudentDetails(name=na, fname=fna, email=mail, qualification=Qua, address=address, phoneno=ph)
    o_ref.save()

    return render(request, 'student/add.html', {"message": "registered!"})
