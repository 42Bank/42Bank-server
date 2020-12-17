import requests
import datetime
from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes
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
    token_json = r.json()
    # print("========================== token_json" , token_json)
    token = token_json['access_token']
    me_url = API_URL + "v2/me"
    # print(token)
    headers = {'Authorization': 'Bearer ' + token}
    r = requests.get(me_url, headers=headers)
    me_content = r.json()
    # print(me_content['login'])
    insert_db(me_content)

    # User(intra_id=me_content['login'], id=me_content['id'], cur_wallet=me_content['wallet']).save()
    # return

    # me_content = r.content
    return HttpResponse(r.json()['login'])
#
def insert_db(info):
    # user
    try:
        if User.objects.filter(intra_id=info['login']):
            pass
        else:
            User(intra_id   = info['login'],
                 user_id    = info['id'],
                 photo      = info['image_url'],
                 cur_wallet = info['wallet']).save()
    except:
        user = User.objects.all()
        user.update(intra_id    = info['login'],
                     user_id    = info['id'],
                     photo      = info['image_url'],
                     cur_wallet = info['wallet'])

    # order
    # try:
    #     User(intra_id   = info['login'],
    #          user_id    = info['id'],
    #          photo      = info['image_url'],
    #          cur_wallet = info['wallet']).save()
    # except:
    #     user = User.objects.all()
    #     user.update(intra_id   = info['login'],
    #                  user_id    = info['id'],
    #                  photo      = info['image_url'],
    #                  cur_wallet = info['wallet'])

    # achvlist
    # try:
    #     User(intra_id   = info['login'],
    #          user_id    = info['id'],
    #          photo      = info['image_url'],
    #          date        = datetime.datetime.now().strftime('%Y%m%d')).save()
    # except:
    #     user = User.objects.all()
    #     user.update(intra_id   = info['login'],
    #                  user_id    = info['id'],
    #                  photo      = info['image_url'],
    #                  date        = datetime.datetime.now().strftime('%Y%m%d'))

    # achved
    try:
        if Achved.objects.filter(user_id=info['id']):
            pass
        else:
            for i in range(0, len(info['achievements'])):
                Achved(user_id     = info['id'],
                       achievement = info['achievements'][i]['name'],
                       date        = datetime.datetime.now().strftime('%Y%m%d')).save()
    except:
        achved = Achved.objects.all()
        for i in range(0, len(info['achievements'])):
            achved.update(user_id     = info['id'],
                          achievement = info['achievements'][i]['name'],
                          date        = datetime.datetime.now().strftime('%Y%m%d'))

    # shop
    # try:
    #     User(intra_id   = info['login'],
    #          user_id    = info['id'],
    #          photo      = info['image_url'],
    #          cur_wallet = info['wallet']).save()
    # except:
    #     user = User.objects.all()
    #     user.update(intra_id   = info['login'],
    #                  user_id    = info['id'],
    #                  photo      = info['image_url'],
    #                  cur_wallet = info['wallet'])

    # notice
    # try:
    #     User(intra_id   = info['login'],
    #          user_id    = info['id'],
    #          photo      = info['image_url'],
    #          date        = datetime.datetime.now().strftime('%Y%m%d')).save()
    # except:
    #     user = User.objects.all()
    #     user.update(intra_id   = info['login'],
    #                  user_id    = info['id'],
    #                  photo      = info['image_url'],
    #                  date        = datetime.datetime.now().strftime('%Y%m%d'))