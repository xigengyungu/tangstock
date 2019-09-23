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
    level = serializers.CharField(source='get_level_display')
    class Meta:
        model = models.Course
        fields = ["id", "name", "course_img", "level"]

class CourseDetailSerializer(serializers.ModelSerializer):
    #o2o o2m
    title = serializers.CharField(source='course.name')
    img = serializers.CharField(source='course.course_img')
    level = serializers.CharField(source='course.get_level_display')

    #m2m
    recommends = serializers.SerializerMethodField()
    class Meta:
        model = models.CourseDetail
        fields = ["course", "title", "img", "level", "course_slogan", "why_study", "recommends"]
        #depth = 2

    def get_recommends(self, obj):
        queryset = obj.recommend_courses.all()
        return [{'id':row.id, 'title':row.name} for row in queryset]

class CourseView1(APIView):
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
            pk = kwargs.get('pk')
            if pk:
                obj = models.Course.objects.filter(id=pk).first()
                ser = CoursesSerializer(instance=obj, many = False)
            else :
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

'''
View
ApiView

'''
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet, ViewSetMixin
class CourseView(ViewSetMixin, APIView):

    def retrieve(self, request, *args, **kwargs):
        ret = {'code':1000, 'data':None}
        try:
            pk = kwargs.get('pk')
            queryset =  models.CourseDetail.objects.filter(course_id=pk).first()
            ser = CourseDetailSerializer(instance=queryset, many=False)
            print ('retrieve——data====',ser.data)
            ret['data'] = ser.data
        except Exception as e:
            print(e)
            ret['code'] = 1001
            ret['error'] = '获取数据无效'

        return Response(ret)
    def list(self, request, *args, **kwargs):
        ret = {'code':1000, 'data':None}
        try:
            queryset =  models.Course.objects.all()
            ser = CoursesSerializer(instance=queryset, many=True)
            print ('list——data====',ser.data)
            ret['data'] = ser.data
        except Exception as e:
            print(e)
            ret['code'] = 1001
            ret['error'] = '获取数据无效'

        return Response(ret)