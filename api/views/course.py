__author__ = 'gujingyun'
# _*_ coding: utf-8 _*_
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import HttpResponse
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.versioning import QueryParameterVersioning, URLPathVersioning
from api import models
from rest_framework import serializers

class CoursesSerializer(serializers.ModelSerializer) :
    class Meta:
        model = models.Course
        fields = "__all__"

class CourseView(APIView):
    #指定返回类型为Json
   # renderer_classes = [JSONRenderer,]
   # versioning_class = URLPathVersioning

    #QueryParameterVersioning  http://127.0.0.1:8000/api/course/?version=v1


    def get(self, request, *args, **kwargs):
        #self.dispatch
        print (request.version)
        '''
        ret = {
            'code':1000,
            'data':[
                {'id':1,'title':'Python全栈'},
                {'id':2,'title':'Linux运维'},
                {'id':3,'title':'金融分析'}
            ]
        }
        '''
        ret = {'code':1000, 'data':None}
        try:
            queryset =  models.Course.objects.all()
            print(queryset)
            ser = CoursesSerializer(instance=queryset, many=True)
            print ('data====',ser.data)
            ret['data'] = ser.data
        except Exception as e:
            print(e)
            ret['code'] = 1001
            ret['error'] = '获取数据无效'

        return Response(ret)
        #return HttpResponse('...')