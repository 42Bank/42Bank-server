import pprint
import requests
from django.shortcuts import render
import webbrowser
from django.http import HttpResponse

# Create your views here.

pp = pprint.PrettyPrinter(indent=4)
API_URL = "https://api.intra.42.fr/"
uid = 'd7e39c6ab1b81ead0f83a923fcebe14c0778a1e16fd7eb24807e377a6e8ab113'
secret = '4fff1b6417d07be99bc2c48649dcb7e328ac0b3bfb58b24ab9d699a3d2cb9a42'

def index(request):
    return HttpResponse("Hello. In this page, you can see crawled data")


def get_token(self):
    CALLBACK = "https%3A%2F%2Fprofile.intra.42.fr"
    API_URL = "https://api.intra.42.fr/"
    # CALLBACK = "http%3A%2F%2F127.0.0.1%3A8000"
    webbrowser.open(
        API_URL + "oauth/authorize?client_id=" + uid + "&redirect_uri=" + CALLBACK + "&response_type=code&scope=public%20forum")
    code = input("Enter code here:")
    data = {
        'grant_type': 'authorization_code',
        'client_id': uid,
        'client_secret': secret,
        'code': code,
        'redirect_uri': 'https://profile.intra.42.fr'
        # 'redirect_uri': 'http://127.0.0.1:8000'
    }
    r = requests.post("https://api.intra.42.fr/oauth/token", data)
    print("Token:", r.content)
    json = r.json()
    self.token = json['access_token']