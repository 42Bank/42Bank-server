import requests
from django.shortcuts import render
from django.http import HttpResponse
import jsons

from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes
from requests_oauthlib import OAuth2Session

from rest_framework import viewsets
from .serializers import *
from .models import *

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
class AchvListView(viewsets.ModelViewSet):
    serializer_class = AchvListSerializer
    queryset = AchvList.objects.all()
class AchvedView(viewsets.ModelViewSet):
    serializer_class = AchvedSerializer
    queryset = Achved.objects.all()
class ShopView(viewsets.ModelViewSet):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()
class NoticeView(viewsets.ModelViewSet):
    serializer_class = NoticeSerializer
    queryset = Notice.objects.all()

# Create your views here.

uid = '0dfca8b2cffc7928d7e207b36879659b90f37e90b90c5e521077ad07ee20a113'
secret = '772317d483a5965bb6cf89cce6c14c46b43111d8f119d5e1668f0f512f8c5904'
CALLBACK = "https%3A%2F%2Fprofile.intra.42.fr"
API_URL = "https://api.intra.42.fr/"
authorize_url = 'https://api.intra.42.fr/oauth/authorize'
redirect_uri = 'http://localhost:3000/main'
scope = 'public'


@api_view(['POST'])
@parser_classes((JSONParser,))
def index(request):
    code = request.data.get('code')
    data = {
        'grant_type': 'authorization_code',
        'client_id': uid,
        'client_secret': secret,
        'code': code,
        'redirect_uri': redirect_uri
    }
    r = requests.post("https://api.intra.42.fr/oauth/token", data)
    json = r.json()
    token = json['access_token']
    me_url = API_URL + "v2/me"
    print(token)
    headers = {'Authorization': 'Bearer ' + token}
    r = requests.get(me_url, headers=headers)
    print("Me:", r.status_code, r.reason)

    return HttpResponse(json['access_token'])