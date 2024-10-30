from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('home', views.home, name='home'),
    path('', views.register, name='register'),
    path('logout', views.logout_view, name='logout'),
]
