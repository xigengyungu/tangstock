__author__ = 'gujingyun'
# _*_ coding: utf-8 _*_
from rest_framework  import serializers
from api import models

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.UserInfo
        fields="__all__"
