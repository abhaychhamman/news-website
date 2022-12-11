from django.db import models

# Create your models here.

class Key(models.Model):
    key = models.CharField(max_length=60)
     
    def __str__(self):
        return str(self.key)
