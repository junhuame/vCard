from django.shortcuts import render, redirect, reverse

def home(request):
    """vCard首页"""
    return render(request, 'index.html')
