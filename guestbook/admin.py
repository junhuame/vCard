from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    """留言消息管理"""
    list_display = ('name', 'email', 'active', 'posted',)
    list_filter = ('active', 'posted')
    search_firlds = ('name', 'message')
    ordering = ('-posted',)


admin.site.register(Message, MessageAdmin)
