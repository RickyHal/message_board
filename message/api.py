# coding:utf-8
from message import models
import uuid
import time


# 将查询结果转list，方便返回给前端读取
def getJson(data):
    res = []
    for item in data:
        if item not in res:
            res.append(item)
    return res


# 获取所有的留言
def get_all_model():
    # 查询所有留言
    messages = getJson((models.Message.objects.all()))
    return messages


# 将从前端获取到的留言内容存储到数据库
def submit_message(request):
    try:
        # 留言id,为生成的uuid
        id = uuid.uuid4()
        # 留言标题
        title = request.POST['title']
        # 留言内容
        message_text = request.POST['message_text']
        # 写入SQLite数据库
        models.Message.objects.create(
            id=id, title=title, message_text=message_text)
        return '提交成功'
    except:
        return '提交失败'
