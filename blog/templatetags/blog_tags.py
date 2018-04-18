from django import template
from blog.models import Post, Category


register = template.Library()


@register.inclusion_tag('latest_posts.html')
def show_latest_posts(count=5):
    """获取最新日志"""
    latest_posts = Post.published_objects.order_by('-publish')[:count]
    return {'latest_posts':latest_posts}


@register.assignment_tag
def get_all_categories():
    """获取日志分类"""
    return Category.objects.all()


