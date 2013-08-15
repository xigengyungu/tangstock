__author__ = 'gujingyun'
#coding=utf-8
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import HttpResponse
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.versioning import QueryParameterVersioning, URLPathVersioning

class CourseView(APIView):
    #指定返回类型为Json
   # renderer_classes = [JSONRenderer,]
   # versioning_class = URLPathVersioning

    #QueryParameterVersioning  http://127.0.0.1:8000/api/course/?version=v1


    def get(self, request, *args, **kwargs):
        #self.dispatch
        print (request.version)
        ret = {
            'code':1000,
            'data':[
                {'id':1,'title':'Python全栈'},
                {'id':1,'title':'Linux运维'},
                {'id':1,'title':'金融分析'}
            ]
        }
        return Response(ret)
        #return HttpResponse('...')