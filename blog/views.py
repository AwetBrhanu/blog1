from django.views import generic
from .models import Post
from django.shortcuts import render
from django.http import HttpResponse


def PostList(request):
    post_list = Post.objects.filter(status=1).order_by('-created_on')
    return render(request, 'index.html', context={'post_list': post_list})

def PostDetail(request):
    model = Post
    template_name = 'post_detail.html'




