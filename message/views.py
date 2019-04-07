# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from message import api
import uuid


# 首页
def index(request):
    # 获取所有的留言，并跳转到首页
    message_list = api.get_all_model()
    return render(request, 'index.html', {'message_list': message_list})


# 跳转到添加留言页面
def add_message(request):
    return render(request, 'add_message.html')


# 获取前端提交的留言信息
def submit_message(request):
    # 只接收POST请求
    if request.method == 'POST':
        # 将从前端收到的留言内容写入数据库
        res = api.submit_message(request)
        return HttpResponse(res)
    else:
        return HttpResponse('请求方式错误')
