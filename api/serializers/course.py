__author__ = 'gujingyun'
# _*_ coding: utf-8 _*_
from rest_framework  import serializers
from api import models

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
    chapers = serializers.SerializerMethodField()

    class Meta:
        model = models.CourseDetail
        fields = ["course", "title", "img", "level", "course_slogan", "why_study", "recommends", "chapers" ]

        #depth = 2

    def get_recommends(self, obj):
        queryset = obj.recommend_courses.all()
        return [{'id':row.id, 'title':row.name} for row in queryset]
    def get_chapers(self, obj):
        queryset=obj.course.coursechapters.all()
        return [{'id':row.id, 'name':row.name} for row in queryset]
