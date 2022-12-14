from django.db import models

# Create your models here.

class Profile(models.Model):
    fullname = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=60)
    username = models.CharField(max_length=60)
    
class UseProfile(models.Model):
    fullname = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=60)
    username = models.CharField(max_length=60)
      
class Profile_info(models.Model):
    username = models.CharField(max_length=60,default="" )
    text = models.CharField(max_length=60)
    img=models.ImageField(upload_to="User/ProfileImage/" ,default="")
    QuotesFav=models.TextField(default="")
    MemesFav=models.TextField(default="")
    JokesFav=models.TextField(default="")

    def __str__(self):
        return str(self.username)
    
    
    