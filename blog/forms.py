from django import forms
# imported from products app
from products.widgets import CustomClearableFileInput
from .models import Comment, BlogPost


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('title', 'image', 'content',)

    image = forms.ImageField(label='Image', required=True,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'image': 'Image',
            'content': 'Blog Content',
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'image':
                self.fields[field].widget.attrs['placeholder'] = (
                    placeholders[field])
            self.fields[field].widget.attrs['class'] = 'blog-form-input'


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        """
        Set auto focus to comment input field, remove
        auto-generated input labels and insert placeholder
        """
        super().__init__(*args, **kwargs)
        self.fields['body'].widget.attrs['placeholder'] = (
            'Write your comment here... (500 characters max).')
        self.fields['body'].label = False
        self.fields['body'].widget.attrs['class'] = 'comment-form-input'
