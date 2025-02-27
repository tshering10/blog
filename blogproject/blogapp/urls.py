
from django.contrib import admin
from django.urls import path
from blogapp.views import Home_view, Detail_view, Addpost_view, category_view, homeview, Update_view, Delete_view

urlpatterns = [
    path('', Home_view.as_view(), name = 'home_view'),
    path('', homeview, name = 'category_home_view'),
    path('post/<int:pk>', Detail_view.as_view(), name = 'detail_view'),
    path('addpost/', Addpost_view.as_view(), name = 'add_post_view'),
    path('post/<int:pk>/edit/', Update_view.as_view(), name = 'update_post_view'),
    path('post/<int:pk>/delete/', Delete_view.as_view(), name = 'delete_post_view'),
    path('category/<slug:category_slug>/', category_view, name = 'category_view'),
]

