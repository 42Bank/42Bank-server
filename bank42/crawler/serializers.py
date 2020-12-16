from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'
class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = '__all__'
class AchvListSerializer(serializers.ModelSerializer):
	class Meta:
		model = AchvList
		fields = '__all__'
class AchvedSerializer(serializers.ModelSerializer):
	class Meta:
		model = Achved
		fields = '__all__'
class ShopSerializer(serializers.ModelSerializer):
	class Meta:
		model = Shop
		fields = '__all__'
class NoticeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Notice
		fields = '__all__'
