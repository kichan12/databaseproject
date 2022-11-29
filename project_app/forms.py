from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model =Post
        fields = ['author', 'title', 'content', 'category',] # author는 일단 추가해놓음
        widgets = {
            'author' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : '',
                },
            ),
            'title' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : '',
                }
            ),
            'content' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : '',
                }
            )
        }
        labels = {
            'author' : '닉네임',
            'title' : '제목',
            'content' : '내용',
            'category' : '카테고리',
        }
        

