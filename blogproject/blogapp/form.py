from django import forms
from .models import Post

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs= {'class': 'form-control'}),
            'author': forms.Select(attrs= {'class': 'form-control'}),
            'body': forms.Textarea(attrs= {'class': 'form-control'}),
        }
        