from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify

from .models import BlogPost
from .forms import CommentForm, BlogPostForm


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
    comments = blog_post.comments.all()
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # Creates new_comment object (doesn't save it)
            new_comment = comment_form.save(commit=False)
            # Assigns the value of what blogpost the user is on
            new_comment.post = blog_post
            # Assigns the username (must be logged in to comment)
            new_comment.username = request.user
            new_comment.save()
            messages.success(request, 'Your comment has been posted!')
            return redirect(reverse('blog_detail', args=[blog_post.slug]))
        else:
            messages.error(request, 'Failed to post your comment. Check that \
                the post is valid and try again.')
    else:
        comment_form = CommentForm()

    context = {
        'blog_post': blog_post,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'blog/blog_detail.html', context)


@login_required
def add_blog_post(request):
    """ Add blog posts to the blog """
    # Allows access to superuser only
    if not request.user.is_superuser:
        messages.error(request, 'Only Hop Shop Admin have \
            access to this page!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.slug = slugify(new_post.title)
            new_post.save()
            messages.success(request, 'Your blog post has been posted!')
            return redirect(reverse('blog_detail', args=[new_post.slug]))
        else:
            messages.error(request, 'Failed to post your blog post. Check that \
                the post is valid and try again.')
    else:
        form = BlogPostForm()

    context = {
        'form': form,
    }

    return render(request, 'blog/add_post.html', context)
