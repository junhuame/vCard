from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count


def blog_list(request):
    """博客列表页"""
    object_list = Post.published_objects.all()
    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog-list.html', {'page': page, 'posts': posts, 'paginator':paginator})


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
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published_objects.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]

    return render(request, 'blog-datail.html', {'post':post, 'similar_posts': similar_posts})