__author__ = 'gujingyun'
from rest_framework.views import APIView
from rest_framework.response import Response

class CourseView(APIView):
    def get(self, request, *args, **kwargs):
        return Response('...')