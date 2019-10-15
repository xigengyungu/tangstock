__author__ = 'gujingyun'
# _*_ coding: utf-8 _*_

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from api import models

#添加认证组件
class TangAuth(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token')
        print('token=',token)
        obj = models.Token.objects.filter(key=token).first()
        if not obj:
            raise AuthenticationFailed({'code':1001, 'error':'认证失败'})
        return (obj.user.username, obj)