from django.urls import path
from . import views

urlpatterns = [
     
    path('signup',views.user_signup),
    path('login',views.user_auth),
    path('email/check',views.check_email),
    
]
