
from django.contrib import admin
from django.urls import path
from django.conf.urls import  url, include
from api.views import course,login,account

urlpatterns = [
    #path('admin/', admin.site.urls),
    #��ʽһ
    #url(r'^course/$', course.CourseView.as_view()),
    #url(r'^course/(?P<pk>\d+)/$', course.CourseView.as_view()),

    url(r'^course/$', course.CourseView.as_view({'get':'list'})),
    url(r'^course/(?P<pk>\d+)/$', course.CourseView.as_view({'get':'retrieve'})),

    url(r'^micro/$', course.MicroView.as_view()),
    url(r'^auth/$', login.LoginView.as_view()),
    #url(r'^auth/$', account.AuthView.as_view()),
]
