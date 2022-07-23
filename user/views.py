from django.shortcuts import redirect, render
from django.contrib import messages
from django.views import View
from .models import userModel
# Create your views here.

class home(View):
    def get(self, request):
        return render(request,'home.html')

class services(View):
    def get(self, request):
        return render(request,'services.html')

class about(View):
    def get(self, request):
        return render(request,'aboutus.html')

class doctors(View):
    def get(self, request):
        return render(request,'doctors.html')

class book(View):
    def get(self, request):
        return render(request,'book.html') 
        
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        message = request.POST.get('message')
        print(name, email, phone, date, time, message)

        user = userModel.objects.create(
            name=name,
            email=email,
            phone=phone,
            date=date,
            time=time,
            message=message
        )
        user.save()
        messages.success(request,"Appointment booked successfully")
        return redirect('book')          