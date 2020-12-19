from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt

from dotenv import load_dotenv
from src import twitch
import os

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
GRANT_TYPE = "client_credentials"


@xframe_options_exempt # Allows iframes on the host extension  
def index(request):

    return HttpResponse("Initial Test")