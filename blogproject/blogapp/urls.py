
from django.contrib import admin
from django.urls import path
from blogapp.views import Home_view, Detail_view, Addpost_view, Update_view, Delete_view, aboutus_view, contact_view

urlpatterns = [
    path('', Home_view.as_view(), name = 'home_view'),
    
    path('post/<int:pk>', Detail_view.as_view(), name = 'detail_view'),
    
    path('addpost/', Addpost_view.as_view(), name = 'add_post_view'),
    
    path('post/<int:pk>/edit/', Update_view.as_view(), name = 'update_post_view'),
    
    path('post/<int:pk>/delete/', Delete_view.as_view(), name = 'delete_post_view'),
    
    path('about/', aboutus_view, name='about_view'),
    
    path('contact/',contact_view, name='contact_us' ),
    # path('contact/success', contact_success, name='contact_us_success' ),
    # path('', base_view, name='home_view'),
    # path('category/', category_view, name='category'),  # Without slug
    # path('category/<int:id>/', category_view, name='category_id')
]


