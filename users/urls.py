# ！/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time   : 2018/6/26 16:40
# @Author : Jerome
from users import views
from django.conf.urls import url

urlpatterns = [
    url(r"^index/$", views.index),
]
