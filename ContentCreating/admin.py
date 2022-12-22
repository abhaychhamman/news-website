from django.contrib import admin
from .models import Channel,Memes,Quotes,News,Jokes
# Register your models here.
admin.site.register(Channel)
admin.site.register(Memes)
admin.site.register(Jokes)
admin.site.register(News)
admin.site.register(Quotes)