# _*_ coding: utf-8 _*_
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

class CourseCategory(models.Model):

    name = models.CharField(max_length=64, unique=True)
    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "课程类"
        verbose_name_plural = "课程类"


class Course(models.Model):
    """
    专题课程
    """
    name = models.CharField(max_length=128, unique=True, verbose_name="模块")
    course_img = models.CharField(max_length=255)
    course_type_choices = ((0, '付费'), (1, 'VIP专享'), (2, '学位课程'))
    course_type = models.SmallIntegerField(choices=course_type_choices)
    brief = models.TextField(verbose_name="课程概述", max_length=2048)
    level_choices = ((0, '初级'), (1, '中级'), (2, '高级'))
    level = models.SmallIntegerField(choices=level_choices, default=1)
    pub_date = models.DateField(verbose_name="发布日期", blank=True, null=True)
    period = models.PositiveIntegerField(verbose_name="建议学习周期(days)", default=7)
    #order = models.IntegerField("课程顺序", help_text="从上一个课程数字往后排")
    attachment_path = models.CharField(max_length=128, verbose_name="课件路径", blank=True, null=True)
    status_choices = ((0, '上线'), (1, '下线'), (2, '预上线'))
    status = models.SmallIntegerField(choices=status_choices, default=0)
    course_category=models.ForeignKey("CourseCategory",on_delete=models.CASCADE,null=True,blank=True)
    #order_details = GenericRelation("OrderDetail", related_query_name="course")
    #coupon = GenericRelation("Coupon")
    #price_policy = GenericRelation("PricePolicy")  # 用于GenericForeignKey反向查询，不会生成表字段，切勿删除，如有疑问请联系老村长

    def __str__(self):
        return "%s(%s)" % (self.name, self.get_course_type_display())

class CourseDetail(models.Model):
    """课程详情页内容"""

    course = models.OneToOneField("Course",on_delete=models.CASCADE)
    hours = models.IntegerField("课时")
    course_slogan = models.CharField(max_length=125, blank=True, null=True)
    video_brief_link = models.CharField(max_length=255, blank=True, null=True)
    why_study = models.TextField(verbose_name="为什么学习这门课程")
    what_to_study_brief = models.TextField(verbose_name="我将学到哪些内容")
    career_improvement = models.TextField(verbose_name="此项目如何有助于我的职业生涯")
    prerequisite = models.TextField(verbose_name="课程先修要求", max_length=1024)
    recommend_courses = models.ManyToManyField("Course", related_name="recommend_by", blank=True)
    #teachers = models.ManyToManyField("Teacher", verbose_name="课程讲师")

    def __str__(self):
        return "%s" % self.course

class CourseChapter(models.Model):
    """课程章节"""
    course = models.ForeignKey("Course", related_name='coursechapters',on_delete=models.CASCADE)
    chapter = models.SmallIntegerField(verbose_name="第几章", default=1)
    name = models.CharField(max_length=128)
    summary = models.TextField(verbose_name="章节介绍", blank=True, null=True)
    is_create = models.BooleanField(verbose_name="是否创建题库进度", default=True)
    pub_date = models.DateField(verbose_name="发布日期", auto_now_add=True)

    class Meta:
        unique_together = ("course", 'chapter')

    def __str__(self):
        return "%s:(第%s章)%s" % (self.course, self.chapter, self.name)
######################################## 用户表 ########################################

from django.utils.safestring import mark_safe

from django.contrib.auth.models import AbstractUser

class UserInfo(models.Model):
    username = models.CharField("用户名", max_length=64, unique=True)
    password = models.CharField("密码", max_length=20)

    def __str__(self):
        return "%s" % (self.username)


class Token(models.Model):
    """
    The default authorization token model.
    """
    key = models.CharField(max_length=40)
    user = models.OneToOneField(
        UserInfo, related_name='auth_token',
        on_delete=models.CASCADE, verbose_name="关联用户"
    )
    created = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)


    def __str__(self):
        return self.key


##############################################################

