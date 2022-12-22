import imp
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from dict.models import Dictionary ,FavDictMean
import requests
import json

# Create your views here.

def dictionary(request):

    if not request.user.is_authenticated:
          return HttpResponseRedirect('/login/')


    if request.method=="POST":
        print(request.POST)
        b = Dictionary(username=request.user,key=request.POST['key'],type=request.POST['type'],mean=request.POST['mean'],synonym=request.POST['synonym'] ,antonym=request.POST['antonym'],example=request.POST['ex'])
        b.save()
        print("add successfully meaning")
        return render(request,"add_meaning.html",context={"msg":"Meaning Added SuccessFully! ...."})

    return render(request,"add_meaning.html")


def index(request):
    if request.method=='POST':


        url=f"https://api.dictionaryapi.dev/api/v2/entries/en/{request.POST['key']}"
        response = requests.request("GET", url)
        # print(response.text)
        res=json.loads(response.text)
        return render(request,"Home.html",context={"data":res})
       

    return render(request,"Home.html")

def contactUs(request):
 
        
    return render(request,"ContactUs.html")


def about(request):
 
        
    return render(request,"about.html")


def show_dict(request):
    if not request.user.is_authenticated:
           
        return HttpResponseRedirect('/login/')
    


    data=Dictionary.objects.all().order_by('key').values()
    c=FavDictMean.objects.filter(username=request.user)
    print([i.favMean for i in c ])
    # print(data[0].example)
    context={
        'data':data,
        'FavMean':[i.favMean for i in c ]
    }
    

    return render(request,"show_dictionary.html",context=context)

@csrf_exempt
def save_data(request):
   

    if request.method == "POST":

        # print(len((str(request.POST['key']).capitalize())),str(request.POST['key']).capitalize()=="Divine")
        res=Dictionary.objects.get(key=str(request.POST['key']))
          
        result={
            "key":res.key,
            "mean":res.mean,
            "type":res.type,
            "synonym":res.synonym,
            "antonym":res.antonym,
            "example":res.example
        }
         
        

        return JsonResponse({'status': result})
    else:
        return JsonResponse({"status": 'fail'})

@csrf_exempt
def saveFav(request):
 

        if request.method == "POST":
            

            c=FavDictMean(username=request.user,favMean=request.POST['Mean'])
            c.save()
        
            return JsonResponse({'status': "pass"})
        else:
            return JsonResponse({"status": 'fail'})
 
       
         
        



