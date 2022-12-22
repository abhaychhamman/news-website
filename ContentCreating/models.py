from django.db import models

# Create your models here.
class Channel(models.Model):
    username = models.CharField(max_length=60,default="Your Name" )
    channelName=models.TextField(default="")
    description=models.TextField(default="very Powerful Content")
    type= models.TextField(default="news")
    logo=models.ImageField(upload_to="ChannelLogo/" ,default="ChannelLogo/default.svg")
 
   
    def __str__(self):
        return str(self.username)
 
    
    
    
class Memes(models.Model):
    id=models.IntegerField(primary_key=True)
    username =models.TextField(default="")
    title = models.CharField(max_length=60,default="" )
    memesImage=models.ImageField(upload_to="UserCreationMemesImage/" ,default="UserCreationMemesImage/default.svg")
    memesType= models.CharField(default="",max_length=130)
    
   
    def __str__(self):
        return str(self.username)
    
    
class Quotes(models.Model):
     
    username =models.CharField(default="",max_length=120)
    userQuotes = models.CharField(max_length=700,default="" )
  
   
    def __str__(self):
        return str(self.username)
 
class Jokes(models.Model):
     
    username =models.CharField(default="",max_length=50)
    type =models.CharField(default="",max_length=200)
    JokesImage=models.ImageField(upload_to="UserCreationJokesmage/" ,default="UserCreationJokesmage/default.svg")
    def __str__(self):
        return str(self.username)
 
    
    
    
 
class News(models.Model):
     
    username =models.CharField(default="",max_length=50)
    newsTitle =models.CharField(default="",max_length=300)
    newsDescription =models.TextField(default="")
    newsContent =models.TextField(default="")
    newsImage=models.ImageField(upload_to="UserCreationNewsImage/" ,default="UserCreationNewsImage/default.svg")
    def __str__(self):
        return str(self.username)
 
    
    
    