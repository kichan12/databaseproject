from django.db import models
from django.views.generic import *
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):                                     # 제품을 분류하기 위한 카테고리 테이블
    name = models.CharField(max_length=15, unique=True)
    slug = models.SlugField(max_length=200, null=True, unique=True, allow_unicode=True) # 카테고리별 url 매핑을 하기위해서 slug 추가 
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'categories'

class Post(models.Model):                                         # 등록 제품 구성 테이블
    id =models.AutoField(primary_key=True)                        # 각 제품마다 등록된 pk 값
    author = models.CharField(max_length=20, blank=True)          # 작성자
    title = models.CharField(max_length=50, blank=True)           # 제품명
    content = models.TextField(max_length=200, blank=True)        # 제품 설명
    created_at = models.DateTimeField(auto_now_add=True)          # 작성 날짜
    updated_at = models.DateTimeField(auto_now=True)              # 갱신 날짜
    category = models.ForeignKey(Category, blank=True, on_delete=models.SET_NULL, null=True) #Category 테이블을 참조하여 동작을 실행
    def __str__(self):
        return f"[{self.id}] {self.title}"

