from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView, LikeView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'), # my code that presents posts in a list
    # path('', views.home, name='blog-home'),
    path('friends/', views.friends, name='blog-friends'),
    path('profile/', views.profile, name='blog-profile'),
    path('contact/<int:senderid>/<int:recipientid>', views.contact, name='blog-contact'),
    path('inbox/', views.inbox, name='blog-inbox'),
    path('demo/', views.demo, name='blog-demo'),
    path('send/', views.SendMessage, name='send_message')
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('profile/', views.profile, name='blog-profile'),
    path('post/<int:pk>/like', LikeView, name='like-post')
]

# <app>/<model>_<viewtype>.html -> looking for blog/post_list.html
