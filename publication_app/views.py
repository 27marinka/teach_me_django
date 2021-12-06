import random

from django.shortcuts import render
from .models import Post

# Create your views here.


def main_page(request):
    #mock_posts = [{"title": random.randint(1, 1000), "text": "sdfdsfdgfdgfdgdsfds"}]
    #posts = Post.objects.all() - возвращает queryset
    posts = Post.objects.filter(is_public=True).order_by('-create_date', '-id',).all()
    context = {'title': 'ПРИВЕТ МИР', 'posts': posts}
    return render(request, 'mainpage.html', context)