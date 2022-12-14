from django.views.decorators.csrf import csrf_exempt
from .models import Profile_info
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
 

@csrf_exempt
def addToFav(request):
    if request.user.is_authenticated:

        
       
        if request.method == "POST":
            c=Profile_info.objects.get(username=request.user)
            if request.POST['type']=="Quotes":             
            
                c.QuotesFav+=request.POST['id']+":"
                c.save()
    
                return JsonResponse({'status': "success"})
            elif request.POST['type']=="Memes":    
                         
                
                return JsonResponse({'status': c.MemesFav})
            
        else:
            return JsonResponse({"status": 'fail'})
    else:
         return JsonResponse({'status': "Login"})

 


  