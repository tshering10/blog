from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})
    
    
    def __str__ (self):
        return self.name
    
   
class Post(models.Model):
    title = models.CharField(max_length = 255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    body = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    
    def __str__ (self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse("detail_view", args = (str(self.id)))
    


class ContactForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"
