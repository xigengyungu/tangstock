
from django.contrib import admin
from django.urls import path
from django.conf.urls import  url, include
from api.views import course

urlpatterns = [
    #path('admin/', admin.site.urls),
    #·½Ê½Ò»
    #url(r'^course/$', course.CourseView.as_view()),
    #url(r'^course/(?P<pk>\d+)/$', course.CourseView.as_view()),

    url(r'^course/$', course.CourseView.as_view({'get':'list'})),
    url(r'^course/(?P<pk>\d+)/$', course.CourseView.as_view({'get':'retrieve'})),
]
