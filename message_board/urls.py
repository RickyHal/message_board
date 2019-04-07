# coding:utf-8

from django.contrib import admin
from django.urls import path
from message import views as message
urlpatterns = [
    # 后台管理系统
    path('admin/', admin.site.urls),
    # 首页
    path('', message.index),
    # 前台添加留言
    path('add_message/', message.add_message),
    # 提交留言
    path('add_message/submit_message/', message.submit_message),
]
