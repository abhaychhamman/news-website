 
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import redirect, render
 
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from .models import UseProfile,Profile_info
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from . import models  
from Quotes.views import Quotes_data 
from django.views.decorators.csrf import  csrf_exempt
 
from .forms import ProfileInfoForm

# Create your views here.

 

def signup(request):
  
    if request.method == 'POST':    
            c=Profile_info(username=request.POST['username'],email=request.POST['email'],)
            c.save()
            
            c=User.objects.create_user(request.POST['username'],request.POST['email'],request.POST['password'])
            c.save()
            print("success")
        
            return HttpResponseRedirect('/login')
   
    return render(request,"signup.html")



def ProfileEditor(request):
    """Process images uploaded by users"""
    if request.method == 'POST':

        c=Profile_info.objects.get(username=request.user)
        print(request.FILES['images'])
        c.img=request.FILES['images']
        c.username=request.POST['username']
        c.age=request.POST['age']
        c.description=request.POST['description']
        c.phone=request.POST['phone']
        c.email=request.POST['email']
        c.save()
        c=User.objects.get(username=request.user)
        c.username= request.POST['username']
        c.save()
           
       
        return HttpResponseRedirect('/profile')
    else:
        form = ProfileInfoForm()
     
        
    return render(request, 'ProfileChanger.html', {'form': form})



@csrf_exempt
def ProfileData(request):
     

    if request.method == "POST":
        if request.user.is_authenticated:
            c=Profile_info.objects.get(username=request.user)
            print(c)
            temp={
                'username':c.username,
                'email':c.email,
                'age':c.age,
                'address':c.address,
                'phone':c.phone,
                'description':c.description,
                
                 }
               

        return JsonResponse(temp )
    else:
        return JsonResponse({"status": 'fail'})



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
                "img": userCurrent.img.url
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
 
     