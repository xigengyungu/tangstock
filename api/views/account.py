__author__ = 'gujingyun'
# _*_ coding: utf-8 _*_
from  rest_framework.response import Response
from  rest_framework.views import APIView
from django.contrib import auth
from django.shortcuts import HttpResponse
from api import models
import uuid
import datetime

class AuthView(APIView):

    def post(self, request, *args, **kwargs):
        print('post ...', request.data)
        ret = {'code':1000}
        username=request.data.get('user')
        password=request.data.get('passwd')
        #user = models.UserInfo.objects.filter(username=username, password=password).first()
        user = auth.authenticate(username=username, password=password)
        if not user:
            ret['code'] = 1001
            ret['error'] = '用户名或密码错误'
        else:
            uid = str(uuid.uuid4())
            now = datetime.datetime.now()
            models.Token.objects.update_or_create(user=user, default={"key":uid,  "created": now})
            print(ret)
            ret['token'] = uid

        return Response(ret)

    def get(self, request, *args, **kwargs):
        print('get ...')
        obj = HttpResponse('...')
        return obj