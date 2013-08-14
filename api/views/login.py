__author__ = 'gujingyun'
# _*_ coding: utf-8 _*_
from  rest_framework.response import Response
from  rest_framework.views import APIView
from django.shortcuts import HttpResponse
from api import models

class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        print('post ...', request.data)
        ret = {'code':1000}
        user=request.data.get('user')
        pwd=request.data.get('passwd')
        user = models.UserInfo.objects.filter(user=user, pwd=pwd).first()
        if not user:
            ret['code'] = 1001

        return Response(ret)

    def get(self, request, *args, **kwargs):
        print('get ...')
        obj = HttpResponse('...')
        return obj