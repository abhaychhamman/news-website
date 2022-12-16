from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
import json
import requests
import random
from Profile  import views
 


url="https://type.fit/api/quotes/"
response = requests.request("GET", url)    
res = json.loads(response.text)

class Quotes_data:
    data=res
           
def quotes(request):
    try:
        if request.user.is_authenticated:
            fav=views.FavQuotes(request)
        else:
            fav=[]
         
        # print(views.FavQuotes(request))
        result=[]
        for i in range(15):
            a=random.randrange(len(res))
            temp=res[a]
            temp['id']=str(a)
            result.append(temp)
         
       
        context = {
                'key':'quotes',
                'quotes':  result ,
                'FavQuotes': fav
            }

    except KeyError:

        context = {

            'starter': ["your daily quata is completed"]
        }

    # es=response.text.encode('utf-8')

    return render(request, "Quotes.html", context)

 