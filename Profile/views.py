 
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect, render
 
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from .models import UseProfile,Profile_info
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from . import models  
from Quotes.views import Quotes_data 
# Create your views here.

 

def signup(request):
  
    if request.method == 'POST':  
        print("start1")
        form = CustomUserCreationForm(request.POST)  
        if form.is_valid():  
            print(form.data['pimg'])
            form.save()  
            c=Profile_info(username=form.data['username'],img=form.data['pimg'])
            c.save()
            print("success")
        
            return HttpResponseRedirect('/login')
  
    else:  
        form = CustomUserCreationForm()  
    context = {  
        'form':form  
    }         
        
    return render(request,"signup.html",context)



def FavQuotes(request):
    c=Profile_info.objects.get(username=request.user)
    format_quotes=c.QuotesFav.split(":")
    Favorite_Quotes=[i for i in format_quotes if i!=""]
    return Favorite_Quotes

def FavJokes(request):
    c=Profile_info.objects.get(username=request.user)
    format=c.JokesFav.split(":")
    Favorite_jokes=[i for i in format if i!=""]
    return Favorite_jokes

def profile(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
       
        
        userCurrent=Profile_info.objects.get(username=request.user)
        # print(str(userCurrent.img).split())
        context={
            'FavQuotes':[Quotes_data.data[int(j)] for j in FavQuotes(request)],
            'profile_info':{

                "name":userCurrent.username,
                "age":userCurrent.age,
                "email":userCurrent.email,
                "phone":userCurrent.phone,
                "address":userCurrent.address,
                "desc":userCurrent.description,
                "img":"http://127.0.0.1:8000/"+str(userCurrent.img)
            }
                }
            

        # return   render(request, 'Profile.html')
        return   render(request, 'Profile.html',context=context)


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
    return   render(request, 'login.html',{'form':AuthenticationForm()})  


def logout_page(request):
    logout(request)
    return    HttpResponseRedirect('/login/')
 
     