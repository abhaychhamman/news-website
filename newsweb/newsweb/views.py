from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def newsweb(request):
    return render(request,"search/navbar.html")
 