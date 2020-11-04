from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import fillform
from django.contrib.auth.models import User ,auth
# Create your views here.
def home(request):

    fill=fillform.objects.all()
    if request.method=='POST':
        name=request.POST['Name']
        email=request.POST['email']
        number=request.POST['Phone Number']
        date=request.POST['dd-mm-yy']
        Time=request.POST['Time']
        service=request.POST['service']
        bikename=request.POST['bikename']

        user=User.objects.create_user(name=name,email=email,number=Phone_number,date=dd-mm-yy,service=service,bikename=bikename)
        user.save();
        print('user created')
        return redirect('/')
    return render(request,'index.html',{'fill':fill})

