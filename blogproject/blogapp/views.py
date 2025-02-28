from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .form import Postform, ContactformModel 
from .models import ContactForm
from django.contrib import messages
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
    
# views for updating blog post
class Update_view(UpdateView):
    model = Post
    template_name = 'blogapp/html/updatepost.html'
    fields = ['title', 'author', 'category','body', ]
    
# views for deleting blog post
class Delete_view(DeleteView):
    model = Post
    template_name = 'blogapp/html/deletepost.html'
    success_url = reverse_lazy('home_view')
    
#About us section view
def aboutus_view(request):
    return render(request, 'blogapp/html/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactformModel(request.POST)
        if form.is_valid():
            # Extract cleaned data from the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Save the data to the database using the model
            messages.success(request, 'Your message has been sent successfully!')
            ContactForm.objects.create(name=name, email=email, message=message)
            
            # Redirect to the success page
            return redirect('home_view')
    else:
        # Initialize the form for GET request
        form = ContactformModel()

    # Render the form in both GET and POST requests
    return render(request, 'blogapp/html/contactus.html', {'form': form})


