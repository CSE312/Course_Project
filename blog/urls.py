from django.urls import path
from . import views
#from . import SendMessage


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('profile/', views.profile, name='blog-profile'),
    path('contact/<int:id>/', views.contact, name='blog-contact'),
    path('inbox/', views.inbox, name='blog-inbox'),
    path('demo/', views.demo, name='blog-demo'),
    path('send/', views.SendMessage, name='send_message')
]
