from django.shortcuts import render

# Create your views here.



 
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect, render
  
from django.contrib.auth.models import User
from .models import Profile_info
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from dict.models import FavDictMean
from . import models  
# Create your views here.
def signup(request):
  
    if request.method == 'POST':  
          
            c=Profile_info(username=request.POST['username'],img=request.FILES['img'],profession=request.POST['profession'])
            c.save()
            c=User.objects.create_user(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
            c.save()
            print("success")
        
            return HttpResponseRedirect('/login')
 
  
 
    return render(request,"Signup.html")



def profile(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:

        context={}
        c=Profile_info.objects.get(username=request.user)
        context['username']=c.username
        context['img']=c.img.url
  
        context['profession']=c.profession
        c=User.objects.get(username=request.user)
        context['email']=c.email 
        
        c=FavDictMean.objects.filter(username=request.user)
        print(c)
        context['FavMean']=[i.favMean for i in c]


        return   render(request, 'Profile.html',context={"profile_info":context})

    else:
        return HttpResponseRedirect('/login/')   


def login_page(request):
    if request.method=='POST':
         
            user=authenticate(username=request.POST['username'],password=request.POST['password'])
            print(user)
            if user is not None:
                login(request,user)
                print(request.user.is_authenticated)
                return HttpResponseRedirect('/profile/')


    if request.user.is_authenticated:
        return HttpResponseRedirect('/profile/')


    return   render(request, 'Login.html',{'form':AuthenticationForm()})  


def logout_page(request):
    logout(request)
    return    HttpResponseRedirect('/login/')
 