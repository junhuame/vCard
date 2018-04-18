from django.contrib import admin
from .models import Category, Post, Comment


class CategoryAdmin(admin.ModelAdmin):
    """日志分类管理"""
    list_display = ('name', 'slug', 'description')


class PostAdmin(admin.ModelAdmin):
    """日志管理"""
    list_display = ('title', 'slug', 'Category', 'status', 'publish')
    list_editable = ('status',)
    search_fields = ('title', 'body')
    date_hierarchy = 'publish'
    list_filter = ('Category', 'status', 'publish')
    list_per_page = 20

    class Media():
        js = (
            'https://cloud.tinymce.com/stable/tinymce.min.js',
            '/static/js/tinymce/custom.js'
        )

class CommentAdmin(admin.ModelAdmin):
    """日志评论管理"""
    list_display = ('name', 'post', 'email', 'active', 'created')
    list_per_page = 20


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)


