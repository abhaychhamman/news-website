from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
import random
def quotes(request):
    try:
        url="https://type.fit/api/quotes"
        response = requests.request("GET", url)
 
        res = json.loads(response.text)
        # for i in res['memes']:

            # print(i['url'])
       
        result=[]
        for i in range(11):
            print(random.randrange(len(res)))
            result.append(res[random.randrange(len(res))])
        
        
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
