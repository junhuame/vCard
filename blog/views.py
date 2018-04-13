from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Post, Comment


def blog_list(request):
    """博客首页"""
    posts = Post.objects.all()
    return render(request, 'blog-list.html', {'posts':posts})
