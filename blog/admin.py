from django.contrib import admin
from .models import BlogPost, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('date_posted', 'title', 'slug')
    search_fields = ['title', 'content']
    inlines = [CommentInline, ]


class CommentAdmin(admin.ModelAdmin):
    list_display = ('date_posted', 'post', 'body', 'username')
    search_fields = ['username', 'body']


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)
