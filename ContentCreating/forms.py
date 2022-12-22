 
from django import forms  
 
from django.forms.forms import Form  


from django import forms
from .models import Memes,Quotes,News,Jokes


class MemesCreationForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Memes
        fields = ('username','title', 'memesImage','memesType',)
        widgets = {'username': forms.HiddenInput()}
            
  
 
class JokesCreationForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Jokes
        fields = ('username','type', 'JokesImage')
        widgets = {'username': forms.HiddenInput()}
            
  
 
class QuotesCreationForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Quotes
        fields = ('username','userQuotes')
        widgets = {'username': forms.HiddenInput()}
            
  
 
class NewsCreationForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = News
        fields = ('username','newsTitle', 'newsDescription','newsContent','newsImage')
        widgets = {'username': forms.HiddenInput()}
            
  
 