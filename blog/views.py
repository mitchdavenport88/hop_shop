from django.shortcuts import render


def blog_posts(request):
    """ A view to return the main blog page """

    return render(request, 'blog/blog.html')
