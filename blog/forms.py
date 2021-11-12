from django import forms
from .models import Comment


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
