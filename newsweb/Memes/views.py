 
from django.shortcuts import render
 
import json
import requests

# Create your views here.



def Memes(request):
    # here create object for retrieve data from database
    try:
        
        
        url = "https://meme-api.herokuapp.com/gimme/wholesomememes/3"
        response = requests.request("GET", url)
 
        res = json.loads(response.text)
        # for i in res['memes']:

        #     print(i['url'])
        context = {
                'key':'Memes',
                'Memes': res['memes']
            }

    except KeyError:

        context = {

            'starter': ["your daily quata is completed"]
        }

    # es=response.text.encode('utf-8')

    return render(request, "Memes/Memes.html", context)
