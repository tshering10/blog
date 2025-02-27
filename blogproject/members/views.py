from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home_view')

    def form_valid(self, form):
        # Save the new user and then show a success message
        response = super().form_valid(form)
        messages.success(self.request, "Your account has been created successfully. You can now log in.")
        return response


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Customize your login template if necessary
    success_url = reverse_lazy('home_view')  # Redirect to home page after successful login

    def get_success_url(self):
        return self.success_url
    
    def  form_valid(self, form):
        messages.success(self.request, 'You have successfully logged in!')
        return super().form_valid(form)
    

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home_view')  # Redirect to home page after successful logout

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'You have successfully logged out!')
        return super().dispatch(request, *args, **kwargs)