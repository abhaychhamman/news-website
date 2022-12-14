 
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
            c=Profile_info(username=form.data['username'], text=form.data['Text'],img=form.data['pimg'])
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
        c=Profile_info.objects.get(username=request.user)
        format_quotes=c.QuotesFav.split(":")
        Favorite_Quotes=[i for i in format_quotes if i!=""]
        lst=[Quotes_data.data[int(j)] for j in Favorite_Quotes]
        print(lst)
            

        return   render(request, 'Profile/Profile.html',context={'FavQuotes':lst})


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
 
     