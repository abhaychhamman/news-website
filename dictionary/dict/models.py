from django.db import models

# Create your models here.

class Dictionary(models.Model):
    username=models.CharField(default="", max_length=50)
    key=models.CharField(max_length=40,unique=True)
    type=models.CharField(max_length=40,default="")
    mean=models.CharField(max_length=200)
    synonym=models.CharField(max_length=40)
    antonym=models.CharField(max_length=40)
    example=models.CharField(max_length=300)

    def __str__(self):
        return  self.key


class FavDictMean(models.Model):
    username=models.CharField( max_length=50)
    favMean=models.CharField( max_length=50)
  

    def __str__(self):
        return  self.username


