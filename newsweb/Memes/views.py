 
from django.shortcuts import render
 
import json
import requests

# Create your views here.



def Memes(request):
    # here create object for retrieve data from database
    try:
        
                
        url = "https://programming-memes-images.p.rapidapi.com/v1/memes/"

        headers = {
            "X-RapidAPI-Key": "f7633fe64bmsh23c17940ff62fe5p167e90jsnf500de6aafc7",
            "X-RapidAPI-Host": "programming-memes-images.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)
 
        res = json.loads(response.text)
        print(res)
       
        context = {
                'key':'Memes',
                'Memes': res[:3]
            }

    except KeyError:

        context = {

            'starter': ["your daily quata is completed"]
        }

    # es=response.text.encode('utf-8')

    return render(request, "Memes/Memes.html", context)
