import os
import ftapi as api
import ssl
import django

from crawler.models import *

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

uid = '0dfca8b2cffc7928d7e207b36879659b90f37e90b90c5e521077ad07ee20a113'
secret = '772317d483a5965bb6cf89cce6c14c46b43111d8f119d5e1668f0f512f8c5904'
name = ['amin', 'jhur', 'hjung']
ftapi = api(uid, secret)

def get_info(self, name):
    data = ftapi.Users(name).Get()
    return data

def get_shop_info(self, campus_id):
    products = ftapi.CampusAllProducts(campus_id).Get()
    return products

def get_achievements(self):
    achv = ftapi.Achievements().Get()
    return achv

if __name__=='__main__':

    # class User(models.Model):
    #     intra_id = models.CharField(max_length=30)
    #     user_id = models.CharField(max_length=30)
    #     photo = models.URLField(blank=True)
    #     cur_wallet = models.SmallIntegerField(default=0)
    for n in name:
        User(intra_id = n, user_id = get_info(n)['id'], photo = 'https://profile.intra.42.fr' + get_info(n)['image_url'], cur_wallet = get_info(n)['wallet']).save()


    # class Order(models.Model):
    #     user_id = models.CharField(max_length=30)
    #     date = models.DateTimeField('checked date')
    #     content = models.CharField(max_length=30)
    #     get_wallet = models.SmallIntegerField(default=0)
    #     spend_wallet = models.SmallIntegerField(default=0)
    #     cur_wallet = models.SmallIntegerField(default=0)


    # class AchvList(models.Model):
    #     title = models.CharField(max_length=30)
    #     wallet_p = models.SmallIntegerField(default=0) <= 없
    achvs = get_achievements()
    for achv in achvs:
        AchvList(title = achv['name']).save()

    # class Achved(models.Model):
    #     user_id = models.CharField(max_length=30)
    #     achievement = models.CharField(max_length=30)
    #     date = models.DateTimeField('checked date') <= 없
    for n in name:
        Achved(user_id = get_info(n)['id'], achievement = get_info(n)['achievements']).save()

    # class Shop(models.Model):
    #     product_id = models.CharField(max_length=30)
    #     name = models.CharField(max_length=30)
    #     price = models.SmallIntegerField(default=0)
    #     photo = models.URLField(blank=True)
    products = get_shop_info('29')
    for pro in products:
        Shop(product_id = pro['id'], name = pro['name'], price = pro['price'], photo = 'https://profile.intra.42.fr' + pro['image']).save()

    # class Notice(models.Model):
    #     date = models.DateTimeField('event date')
    #     title = models.CharField(max_length=30)
    #     price = models.CharField(max_length=30)