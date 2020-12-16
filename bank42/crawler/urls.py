from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='crawler_index'),
    # path('auth/', views.get_token, name='get_token'),
]
