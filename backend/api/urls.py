from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('create-order/', views.create_order, name='create-order'),
    path('signup/', views.signup_user, name='signup'),
]
