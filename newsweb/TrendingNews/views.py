 
from django.shortcuts import render
 
import json
import requests

# Create your views here.



def TrendingNews(request):
    # here create object for retrieve data from database
    try:
        
        url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/search/NewsSearchAPI"
        headers = {
                'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
                'x-rapidapi-key': "066ad0e562mshf1cc56af4b67393p1cf041jsnd2a8c95bf42c"
            }
        querystring = {'q': 'Trending News', "pageNumber": "1", "pageSize": "50", "autoCorrect": "true",
                           "fromPublishedDate": "null", "toPublishedDate": "null"}

          

        response = requests.request(
                "GET", url, headers=headers, params=querystring)
        # request for api
        res = json.loads(response.text)
        print(res['value'][1]['image']['url'])
        context = {
                'key':'Trending News',
                'news_res': res['value']
            }

    except KeyError:

        context = {

            'starter': ["your daily quata is completed"]
        }

    # es=response.text.encode('utf-8')

    return render(request, "TrendingNews/TrendingNews.html", context)
