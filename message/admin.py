# coding:utf-8
from django.contrib import admin

from message import models


class MessageAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Message, MessageAdmin)
