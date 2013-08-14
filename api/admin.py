from django.contrib import admin

from .models import *
admin.site.register(UserInfo)
admin.site.register(Course)
admin.site.register(CourseDetail)
admin.site.register(CourseChapter)
# Register your models here.
