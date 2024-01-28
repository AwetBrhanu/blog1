from . import views
from django.urls import path
urlpatterns = [
    path('', views.PostList, name='home'),
    path('post/', views.PostDetail, name='post_detail'),
] 
