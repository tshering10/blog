
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls')),
    path('members/login/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]
