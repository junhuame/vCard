# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-12 13:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='分类名称')),
                ('slug', models.SlugField(verbose_name='URl缩写')),
                ('description', models.CharField(max_length=200, null=True, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='用户名')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('content', models.TextField(verbose_name='评论')),
                ('active', models.BooleanField(default=True, verbose_name='有效状态')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='提交时间')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('slug', models.SlugField(max_length=100, unique_for_date='publish', verbose_name='URL缩写')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='图片')),
                ('body', models.TextField(verbose_name='正文')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发布时间')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('status', models.CharField(choices=[('draft', '草稿'), ('published', '发布')], default='draft', max_length=50, verbose_name='发布状态')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to='blog.Category')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-publish'],
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Post'),
        ),
    ]
