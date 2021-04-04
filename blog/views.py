from django.shortcuts import render, redirect
from .models import Post
from authentication.models import Profile
from django.contrib.auth.decorators import login_required
from authentication.forms import PictureUpdateForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def get_all_logged_in_users():
    unexpired_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    logged_in = []

    for session in unexpired_sessions:
        temp = session.get_decoded()
        if temp and Profile.objects.filter(user_id=temp['_auth_user_id'])[0] not in logged_in:
            logged_in.append(Profile.objects.filter(user_id=temp['_auth_user_id'])[0])

    return logged_in


def get_all_users():
    signed_up = Profile.objects.all()
    return signed_up


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/Home.html', context)


def demo(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/demo.html', context)


# Create your views here.
@login_required
def friends(request):
    profiles = get_all_users()
    logged_in = get_all_logged_in_users()
    context = {'profile': profiles, 'logged_in': logged_in}  # this is the old code with all signed up users
    # displaying context = {'posts': Post.objects.all(), 'logged_in': logged_in} #
    # Me trying to combine posts and users -> doesnt work
    # context = {'posts': Post.objects.all()}
    return render(request, 'blog/Friends.html', context)
    # return render(request, 'blog/Home.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        info_form = UserUpdateForm(request.POST, instance=request.user)
        picture_form = PictureUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if info_form.is_valid() and picture_form.is_valid():
            info_form.save()
            picture_form.save()
            messages.success(request, f'Account Successfully Updated!')
            return redirect('/blog/profile')
    else:
        info_form = UserUpdateForm(instance=request.user)
        picture_form = PictureUpdateForm(instance=request.user.profile)

    context = {
        'info_form': info_form,
        'picture_form': picture_form
    }

    return render(request, 'blog/Profile.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/Home.html'  # <app>/<model>_<viewtype>.html
    content_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)  # setting author as current user before post is ran


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
