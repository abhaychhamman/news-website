from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
import json
import requests
import random


url="https://type.fit/api/quotes/"
response = requests.request("GET", url)    
res = json.loads(response.text)

class Quotes_data:
    data=res
           
def quotes(request):
    try:
      
       
        result=[]
        for i in range(11):
            a=random.randrange(len(res))
            temp=res[a]
            temp['id']=a
            result.append(temp)
       
        context = {
                'key':'quotes',
                'quotes':  result 
            }

    except KeyError:

        context = {

            'starter': ["your daily quata is completed"]
        }

    # es=response.text.encode('utf-8')

    return render(request, "quotes/quotes.html", context)

 
