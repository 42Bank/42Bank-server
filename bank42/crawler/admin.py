from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(User)
admin.site.register(Order)
admin.site.register(AchvList)
admin.site.register(Achved)
admin.site.register(Shop)
admin.site.register(Notice)