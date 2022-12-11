 
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect, render
 
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from .models import UseProfile,Profile_info
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from . import models  
# Create your views here.
def signup(request):
  
    if request.method == 'POST':  
        print("start1")
        form = CustomUserCreationForm(request.POST)  
        if form.is_valid():  
            print(form.data['pimg'])
            form.save()  
            c=Profile_info(username=form.data['username'], text=form.data['Text'])
            c.save()
            print("success")
        
            return HttpResponseRedirect('/profile')
  
    else:  
        form = CustomUserCreationForm()  
    context = {  
        'form':form  
    }         
        
    return render(request,"Profile/signup.html",context)



def profile(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return   render(request, 'Profile/Profile.html')

    else:
        return HttpResponseRedirect('/login/')   
def login_page(request):
    if request.method=='POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            print(user)
            if user is not None:
                login(request,user)
                print(request.user.is_authenticated)
                return HttpResponseRedirect('/profile/')
    return   render(request, 'Profile/login.html',{'form':AuthenticationForm()})  


def logout_page(request):
    logout(request)
    return    HttpResponseRedirect('/login/')

def UserProfile(request):
    if request.method == 'POST':  
        print("stat1")
        username=request.POST.get('Username')
        fname=request.POST.get('fname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        b=UseProfile(username= username,fullname= fname,email=email,password=password)
        b.save()
        print(username,fname,email,password)
  
    else:  
        print("something went wrong")
 
        
    return render(request,"Profile/UserProfile.html")
     