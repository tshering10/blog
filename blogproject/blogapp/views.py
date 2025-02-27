from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .form import Postform 

#listing all the blog posts
class Home_view(ListView):
    model = Post
    template_name = 'blogapp/html/home.html'
    ordering = ['-id']

class Detail_view(DetailView):
    model = Post
    template_name = 'blogapp/html/details.html'
    context_object_name = 'post'
    
class Addpost_view(CreateView):
    model = Post
    form = Postform
    template_name = 'blogapp/html/addpost.html'
    fields = '__all__'
    success_url = reverse_lazy('home_view')
    
def category_view(request, category_slug):
    posts = Post.objects.filter(category_slug = category_slug)
    context = {
        'posts': posts,
        'category_slug': category_slug
    }
    return render(request, 'blogapp/html/category.html', context)

#category view
def homeview(request):
    categories = Category.objects.all()
    return render(request, 'blogapp/html/home.html', {'categories': categories})

# views for updating blog post
class Update_view(UpdateView):
    model = Post
    template_name = 'blogapp/html/updatepost.html'
    fields = ['title', 'body']
    
# views for deleting blog post
class Delete_view(DeleteView):
    model = Post
    template_name = 'blogapp/html/deletepost.html'
    success_url = reverse_lazy('home_view')
    
