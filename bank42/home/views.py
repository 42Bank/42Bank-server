from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
import json
# Create your views here.
# def index(request):
#     return HttpResponse("Hello. This is HOME")
# class IndexView(View):
    # def post(self, request):
        # return HttpResponse("Post 요청 받음")

from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes


@api_view(['GET'])
@parser_classes((JSONParser,))
def index(request):
    foo = request.data.get('code')
    # bar = request.data.get('bar')

    return JsonResponse({
        'code': foo,
        # 'bar': bar
    })
