from django.shortcuts import render, get_object_or_404

from .models import BlogPost


def blog_posts(request):
    """ A view to return the main blog page """
    posts = BlogPost.objects.all()
    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)


def blog_detail(request, slug):
    """ A view that returns individual blog posts products """
    blog_post = get_object_or_404(BlogPost, slug=slug)
    context = {
        'blog_post': blog_post,
    }

    return render(request, 'blog/blog_detail.html', context)
