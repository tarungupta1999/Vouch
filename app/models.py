from django.db import models


# Create your models here.
class Tweets(models.Model):    
    id = models.CharField(max_length=100,primary_key = True)
    Name = models.CharField(max_length=100)
    User = models.CharField(max_length=1000)
    Tweet_id = models.CharField(max_length=100)
    Tweet = models.CharField(max_length=1000)    
    Dom = models.CharField(max_length=1000)
    Profile_picture = models.CharField(max_length=100)