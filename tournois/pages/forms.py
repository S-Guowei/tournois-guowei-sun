from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    model = Comment
    fields = ['body','user']
    

