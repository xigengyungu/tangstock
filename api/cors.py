__author__ = 'gujingyun'
from django.middleware.common  import CommonMiddleware
#from django.utils.deprecation import MiddlewareMixin

class MiddlewareMixin:
    def __init__(self, get_response=None):
        self.get_response = get_response
        super().__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        response = response or self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response

class CORSMiddleware  (MiddlewareMixin):
    def process_response(self, request, response):
        #�����Ӧͷ
        #�������
        print('CORSMiddleware ...',request.method)
        response['Access-Control-Allow-Origin']="*"
        #����Я��Content-Type
        if request.method == "OPTIONS":
            response['Access-Control-Allow-Headers']="Content-Type"
            #������
            response['Access-Control-Allow-Methods']="DELETE,PUT,POST"


        return response