__author__ = 'gujingyun'
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import HttpResponse
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

class CourseView(APIView):
    #ָ����������ΪJson
    renderer_classes = [JSONRenderer,]

    def get(self, request, *args, **kwargs):
        return Response('...')
        #return HttpResponse('...')