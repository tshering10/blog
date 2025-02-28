from django import forms
from .models import Post, ContactForm

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'category', 'body']
        widgets = {
            'title': forms.TextInput(attrs= {'class': 'form-control'}),
            'author': forms.Select(attrs= {'class': 'form-control'}),
            'category': forms.Select(attrs= {'class': 'form-control'}),
            'body': forms.Textarea(attrs= {'class': 'form-control'}),
        }

class ContactformModel(forms. ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'message']