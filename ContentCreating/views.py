from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from Profile.models import Profile_info
from django.contrib.auth.models import User
from .models import Channel,Memes,Jokes,Quotes,News
from .forms import MemesCreationForm,JokesCreationForm,QuotesCreationForm,NewsCreationForm
from django.views.decorators.csrf import  csrf_exempt
# Create your views here.

def UserChannel(request,user):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
     
    c=Channel.objects.get(username=user)
    if c.type=="Memes":
         
        UserAllContent=Memes.objects.filter(username=user)
    elif c.type=="Quotes":
        
        UserAllContent=Quotes.objects.filter(username=user)
    elif c.type=="News":
        UserAllContent=News.objects.filter(username=user)
       
      
    elif c.type=="Jokes":
        UserAllContent=Jokes.objects.filter(username=user)
        print(UserAllContent[0].JokesImage.url)
 
        
    

    return render(request,'ChannelProfile.html',context={'ChannelProfile':c,'UserAllContent':UserAllContent})


@csrf_exempt
def ChannelData(request):
     

    if request.method == "POST":
        if request.user.is_authenticated:
            c=Channel.objects.get(username=request.user)
            data={

                'channel':c.channelName,
                'type':c.type,
                'desc':c.description,
                'logo':c.logo.url,
            }
           
               

        return JsonResponse(data)
    else:
        return JsonResponse({"status": 'fail'})

 

def EditChannel(request):
     
    if request.method == 'POST':
        c=Channel.objects.get(username=request.user)
        c.logo=request.FILES['images']
        c.description=request.POST['description']
        c.channelName=request.POST['channelName']
        c.type=request.POST['channelType']
        c.save()

        return  HttpResponseRedirect('/Channel/'+str(request.user))

    

    return render(request,'EditChannel.html')


def ContentPage(request):






    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
   

    if Channel.objects.filter(username=request.user).count()>=1:
        return HttpResponseRedirect('/Channel/'+str(request.user))


    if request.method=='POST':
      
       
        c=Channel(username=request.user,description=request.POST['description'],type=request.POST['channelType'],logo=request.FILES['images'])

   
        c.save()
        c=Profile_info.objects.get(username=request.user)
       
        c.isChannel=True
        c.save()
      
        return  HttpResponseRedirect('/Channel/'+str(request.user))
  

   


    return render(request,'CreateChannelPage.html')


def ContentCreation(request,channelType):
    
    if channelType=="Memes":
        form=MemesCreationForm() 
    elif channelType=="Quotes":
        form=QuotesCreationForm() 
    elif channelType=="News":
        form=NewsCreationForm()
      
    elif channelType=="Jokes":
        form=JokesCreationForm()
        
  
    if request.method=="POST":
  
        if channelType=="Memes":
            form=MemesCreationForm()
            c=Memes(username=request.user,title=request.POST['title'],memesType=request.POST['memesType'],memesImage=request.FILES['memesImage'])
       
        elif channelType=="Quotes": 
            c=Quotes(username=request.user,userQuotes=request.POST['userQuotes'])
        elif channelType=="News": 
            c=News(username=request.user,newsTitle=request.POST['newsTitle'],newsDescription=request.POST['newsDescription'],newsImage=request.FILES['newsImage'],newsContent=request.POST['newsContent'])
        elif channelType=="Jokes": 
            c=Jokes(username=request.user,type=request.POST['type'],JokesImage=request.FILES['JokesImage'])
      
        c.save()
        return  HttpResponseRedirect('/Channel/'+str(request.user))
         

    return render(request,"ContentCreation.html",context={'form':form,"channelType":channelType})
 
