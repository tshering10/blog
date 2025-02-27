from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    
class Loginview(LoginView):
    template_name = 'registration/login.html'
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            return reverse_lazy('home')  # You can change this to any named view you prefer
        return super().get_redirect_url()  