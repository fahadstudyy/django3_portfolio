from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blog(request):
    blog_count = Blog.objects.count
    blogs = Blog.objects.order_by('-date')[:3]
    return render(request, 'Blog/all_blogs.html', {'blogs': blogs, 'blog_count': blog_count})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'Blog/detail.html',{'blog': blog})
