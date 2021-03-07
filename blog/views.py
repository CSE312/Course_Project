from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from authentication.forms import PictureUpdateForm, UserUpdateForm
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone


def get_all_logged_in_users():
    # Query all non-expired sessions
    # use timezone.now() instead of datetime.now() in latest versions of Django
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    uid_list = []

    # Build a list of user ids from that query
    for session in sessions:
        data = session.get_decoded()
        uid_list.append(data.get('_auth_user_id', None))

    # Query all logged in users based on id list
    return User.objects.filter(id__in=uid_list)

# Create your views here.
@login_required
def home(request):
    k = get_all_logged_in_users()
    print(k)
    return render(request, 'blog/Home.html')


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


def demo(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/demo.html', context)
