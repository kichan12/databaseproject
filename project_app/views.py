from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, TemplateView
from .forms import PostForm
from .models import Post, Category
from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import CreateView
from .forms import PostForm
from .models import Post
from django.urls import reverse

import ast

def home(request):
    post_objects = Post.objects.order_by('-created_at')
    context = {'post_objects' : post_objects}    
    return render(request, 'index.html', context)
def post_list(request):
    post_objects = Post.objects.order_by('-created_at')
    context = {'post_objects' : post_objects}
    return render(request, 'post_list.html', context)


        
def categoryview(request,category_slug=None):
    current_category=None
    categories=Category.objects.all()
    if category_slug:
        current_category=get_object_or_404(Category,slug=category_slug)
        products=Post.objects.filter(category=current_category)
        return render(request,'categories.html',
                    {
                        'current_category':current_category,
                        'categories':categories,
                        'products':products
                    })

