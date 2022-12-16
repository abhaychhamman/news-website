from django.shortcuts import render

# Create your views here.
import requests
import json


def memes(request):
    url = "https://programming-memes-reddit.p.rapidapi.com/"

    headers = {
        "X-RapidAPI-Key": "b074fc0f12mshde9f23386b948b0p159763jsn0a3570621e18",
        "X-RapidAPI-Host": "programming-memes-reddit.p.rapidapi.com",
        
    }

    response = requests.request("GET", url, headers=headers)
 
    res=json.loads(response.text)    


    return render(request,"Memes.html",context={"Memes":res[:6]})