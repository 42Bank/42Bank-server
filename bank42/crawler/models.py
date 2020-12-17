from django.db import models


# Create your models here.
class User(models.Model):
    intra_id = models.CharField(max_length=30)
    user_id = models.CharField(max_length=30)
    photo = models.URLField(blank=True)
    cur_wallet = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.intra_id

class Order(models.Model):
    user_id = models.CharField(max_length=30)
    date = models.CharField(max_length=8)
    content = models.CharField(max_length=30)
    get_wallet = models.SmallIntegerField(default=0)
    spend_wallet = models.SmallIntegerField(default=0)
    cur_wallet = models.SmallIntegerField(default=0)

class AchvList(models.Model):
    title = models.CharField(max_length=30)
    wallet_p = models.SmallIntegerField(default=0)

class Achved(models.Model):
    user_id = models.CharField(max_length=30)
    achievement = models.CharField(max_length=30)
    date = models.CharField(max_length=8)

class Shop(models.Model):
    product_id = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    price = models.SmallIntegerField(default=0)
    photo = models.URLField(blank=True)

class Notice(models.Model):
    date = models.CharField(max_length=8)
    title = models.CharField(max_length=30)
    price = models.CharField(max_length=30)

