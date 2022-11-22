from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, TemplateView
from .forms import PostForm, ScheduleForm
from .models import Post, Schedule, Category
from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import CreateView
from .forms import PostForm
from .models import Post, Comment
from django.urls import reverse

import ast

def home(request):
    post_objects = Post.objects.order_by('-created_at')
    context = {'post_objects' : post_objects}
    
    return render(request, 'index.html', context)

def team_intro(request):
    return render(request, 'backend_team.html')

def post_list(request):
    post_objects = Post.objects.order_by('-created_at')
    context = {'post_objects' : post_objects}
    return render(request, 'post_list.html', context)

def post_detail(request, pk):
    post_detail_object = Post.objects.get(pk=pk)
    schedule_detail_object = Schedule.objects.get(post_id=pk)
    sequence_list = ast.literal_eval(schedule_detail_object.sequence) # str 형태의 리스트를 list 형태로 바꿔주는 메서드입니다. 
    place_list = ast.literal_eval(schedule_detail_object.place)
    detail_list = ast.literal_eval(schedule_detail_object.detail_content)
    schedule_loop = zip(sequence_list, place_list, detail_list)
    return render(request, 'post_detail.html',{'post_detail_object':post_detail_object,'comment_form':comment_form, 'schedule_loop':schedule_loop})

def post_create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        schedule_form = ScheduleForm(request.POST)
        context = {'post_form':post_form, 'schedule_form':schedule_form}
        if schedule_form.is_valid():
            schedule = schedule_form.save(commit=False)
            schedule.sequence = request.POST.getlist('sequence')
            schedule.place = request.POST.getlist('place')
            schedule.detail_content = request.POST.getlist('detail_content')
            if post_form.is_valid():
                post = post_form.save() # post_form이 DB에 저장됨.
                # post_form DB에 저장된 내용 중 post_id에 해당하는 값을 schedule_form의 post_id에 저장해야 한다.
                schedule.post_id = post.pk
                schedule_form.save()
                return redirect('post_list')
        else:
            return render(request, 'post_create.html', context)
    else:
        post_form = PostForm(request.POST)
        schedule_form = ScheduleForm(request.POST)
        context = {'post_form':post_form, 'schedule_form':schedule_form}
        return render(request, 'post_create.html', context)
        
def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    schedule_obj = Schedule.objects.get(post_id=pk)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        schedule_form = ScheduleForm(request.POST, instance=schedule_obj)
        context = {'post_form':post_form, 'schedule_form':schedule_form}
        if schedule_form.is_valid():
            schedule = schedule_form.save(commit=False)
            schedule.sequence = request.POST.getlist('sequence')
            schedule.place = request.POST.getlist('place')
            schedule.detail_content = request.POST.getlist('detail_content')
            if post_form.is_valid():
                post = post_form.save(commit=False)
                schedule.post_id = post.pk
                post.created_at = post.updated_at
                post_form.save()
                schedule_form.save()
            return redirect('post_detail', post.pk)
    else:
        post_form = PostForm(instance=post) # instance = post 를 사용하면 post에 저장되어 있던 이전 내용들을 모두 불러옵니다.
        sequence_list = ast.literal_eval(schedule_obj.sequence) # str 형태의 리스트를 list 형태로 바꿔주는 메서드입니다. 
        place_list = ast.literal_eval(schedule_obj.place)
        detail_list = ast.literal_eval(schedule_obj.detail_content)
        schedule_loop = zip(sequence_list, place_list, detail_list)
        context = {'post_form':post_form, 'schedule_loop':schedule_loop}
        return render(request, 'post_edit.html', context)

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
        
def company_list(request):
    return render(request, 'company_list.html')

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

