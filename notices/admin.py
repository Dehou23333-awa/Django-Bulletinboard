from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Notice

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date','is_pinned')  # 在列表页面显示 is_pinned 字段
    list_editable = ('is_pinned',)
    
admin.site.register(Notice, NoticeAdmin)