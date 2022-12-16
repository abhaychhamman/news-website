from django.shortcuts import render
from django.http import HttpResponse
import json
import requests

url="https://v2.jokeapi.dev/joke/Any?amount=10"
response = requests.request("GET", url)
res = json.loads(response.text)
    


def jokes(request):
    try:
       
        # for i in res['memes']:

            # print(i['url'])
        context = {
                'key':'jokes',
                'jokes':  res['jokes'] 
            }

    except KeyError:

        context = {

            'starter': ["your daily quata is completed"]
        }

    # es=response.text.encode('utf-8')

    return render(request, "Jokes.html", context)