from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('profile/', views.profile, name='blog-profile'),
    path('contact/<int:id>/', views.contact, name='blog-contact'),
    path('messages/', views.myMessages, name='blog-messages'),
    path('demo/', views.demo, name='blog-demo')
]
