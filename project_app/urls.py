from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = 'home'),
    path('post_list/', views.post_list, name = 'post_list'), #게시글목록
    path('search/',include('search.urls')),
    path('',include('accounts.urls')),
    path('<slug:category_slug>/',views.categoryview,name="category" ),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
