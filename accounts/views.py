from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def signup(request):
    if request.method=="POST":
        first_name =  request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST['email']

        if str(password1)== str(password2):
            user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password1,email=email)
            user.save()
            return render(request,"events.html")
        else:
            print("password not matched")
    return  render(request,"login.html")

def login(request):
    if request.method=="POST":
        username = request.POST.get('username_login')
        password = request.POST.get('password_login')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print("logged in")
            return redirect("/")

        else:
            messages.info(request,'invalid info')
            print("login failed")

            return redirect("/")
    return render(request,"login.html")