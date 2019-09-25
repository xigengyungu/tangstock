__author__ = 'gujingyun'
# _*_ coding: utf-8 _*_
from  rest_framework import response
from  rest_framework.views import APIView
from django.shortcuts import HttpResponse

class LoginView(APIView):
    def options(self, request, *args, **kwargs):
        obj = HttpResponse('...')
        obj['Access-Control-Allow-Origin']="*"
        obj['Access-Control-Allow-Headers']="Content-Type"
        print('options ....')
        return obj

    def post(self, request, *args, **kwargs):
        print('post ...')
        obj = HttpResponse('...')
        obj['Access-Control-Allow-Origin']="*"
        return obj

    def get(self, request, *args, **kwargs):
        print('get ...')
        obj = HttpResponse('...')
        return obj