from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Post, Comment


def blog_list(request):
    """博客首页"""
    posts = Post.objects.all()
    return render(request, 'blog-list.html', {'posts':posts})


def blog_datail(request, year, month, day, slug):
    """博客日志详情页"""
    post = get_object_or_404(
        Post, 
        slug = slug,
        publish__year = year,
        publish__month = month,
        publish__day = day,
        status = 'published'
        )
    return render(request, 'blog-datail.html', {'post':post})