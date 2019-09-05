
from django.contrib import admin
from django.urls import path
from django.conf.urls import  url, include
from api.views import course

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^(?P<version>[v1|v2]+)/course/$', course.CourseView.as_view()),
]
