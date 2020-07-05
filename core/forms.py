from django import forms
from . models import Post


class NewsForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'content']
