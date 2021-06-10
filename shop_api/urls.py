from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='main-page'),
    path('regist/', views.register, name='register'),
    path('login/', views.login_check, name='login'),
]