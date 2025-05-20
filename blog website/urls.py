from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),

]
