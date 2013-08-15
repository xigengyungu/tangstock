__author__ = 'gujingyun'
# _*_ coding: utf-8 _*_
from  rest_framework.response import Response
from  rest_framework.views import APIView
from django.shortcuts import HttpResponse
from api import models
import uuid
import datetime

class AuthView(APIView):

    def post(self, request, *args, **kwargs):
        print('post ...', request.data)
        ret = {'code':1000}
        user=request.data.get('user')
        pwd=request.data.get('passwd')
        user = models.UserInfo.objects.filter(user=user, pwd=pwd).first()
        if not user:
            ret['code'] = 1001
            ret['error'] = '用户名或密码错误'
        else:
            uid = str(uuid.uuid4())
            models.Token.objects.update_or_create(user=user, default={'key':uid,  "created": datetime.datetime.now()})
            ret['token'] = uid

        return Response(ret)

    def get(self, request, *args, **kwargs):
        print('get ...')
        obj = HttpResponse('...')
        return obj