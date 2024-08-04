from django.shortcuts import render
from django.shortcuts import HttpResponse
from.models import Posts

def community(request):
      posts = Posts.objects.all().order_by('-date')
      return render(request, 'post4/post.html',{'posts': posts})

def post_page(request, slug):
      post = Posts.objects.get(slug=slug)
      return render(request, 'post4/post_page.html',{'post': post})

