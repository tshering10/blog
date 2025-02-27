from django.urls import path
from members.views import RegisterView, CustomLoginView, CustomLogoutView

urlpatterns = [
    # Registration URL
    path('register/', RegisterView.as_view(), name='register_view'),
    
    # Login URL
    path('login/', CustomLoginView.as_view(), name='login'),
    
    # Logout URL
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    
]

    # path('login/', Loginview.as_view(), name='login'),
    # path('logout/', Logoutview.as_view(), name='logout'),

