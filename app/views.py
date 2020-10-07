import tweepy
from django.http import HttpResponseRedirect
from .models import *
from django.db.models import Count
from datetime import date, timedelta



Consumer_Key='x4r61WB5uIkBETpUkjWdyzefa'
Consumer_Secret='nPkO03AvlEpvFELCVCydn7GT5mXkbHoC6vGTXpf8g7xFp7wVGH'

# Create your views here.



def login(request):
    oauth=tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)
    try:
        redirect_url = oauth.get_authorization_url(True)
    except tweepy.TweepError:
        print('Error! Failed to get request token.')
    request.session['request_token']= oauth.request_token    
    return HttpResponseRedirect(redirect_url)

