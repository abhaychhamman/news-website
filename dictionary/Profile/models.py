from django.db import models

# Create your models here.


class Profile_info(models.Model):
    username= models.CharField(max_length=60)
    img= models.ImageField(upload_to="profileImage/",default="profile.png")
    profession= models.CharField(max_length=60)


    def __str__(self) -> str:
        return self.username