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
    username = models.CharField(max_length=60,default="Your Name" )
    img=models.ImageField(upload_to="ProfileImage/" ,default="logo.svg")
    age=models.IntegerField(default=0)
    address=models.TextField(default="india")
    phone=models.TextField(default="1234567890")
    email=models.EmailField(default="example123@.com", max_length=254)
    description=models.TextField(default="i am a programmer")
    QuotesFav=models.TextField(default="")

    def __str__(self):
        return str(self.username)
    
    
    