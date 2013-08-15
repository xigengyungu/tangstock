__author__ = 'gujingyun'
# _*_ coding: utf-8 _*_

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from api import models

class TangAuth(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token')
        obj = models.Token.objects.filter(key=token)
        if not obj:
            raise AuthenticationFailed({'code':1001, 'error':'认证失败'})
        return (obj.user.user, obj)