from django.contrib import admin
from .models import Post, Category, ContactForm
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author']
    list_per_page=3
admin.site.register(Category)
admin.site.register(ContactForm)

