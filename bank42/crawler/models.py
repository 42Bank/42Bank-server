from django.db import models


# Create your models here.
class User(models.Model):
    intra_id = models.CharField(max_length=30)
    user_id = models.CharField(max_length=30)
    photo = models.URLField(blank=True)
    cur_wallet = models.SmallIntegerField(default=0)
