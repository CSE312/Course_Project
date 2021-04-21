from django.shortcuts import render, redirect
from .models import Post
from authentication.models import Profile
from direct_message.models import Message
from django.contrib.auth.decorators import login_required
from authentication.forms import PictureUpdateForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone


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


# Create your views here.
@login_required
def home(request):
    messages = Message.get_messages(user=request.user)
    i = 0
    for message in messages:
        if message.is_read == False:
            i = i + 1
    profiles = get_all_users()
    logged_in = get_all_logged_in_users()
    context = {'profile': profiles, 'logged_in': logged_in, 'unread': i}
    return render(request, 'blog/Home.html', context)


@login_required
def profile(request):
    messages = Message.get_messages(user=request.user)
    i = 0
    for message in messages:
        if message.is_read == False:
            i = i + 1
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
        'picture_form': picture_form, 
        'unread': i
    }

    return render(request, 'blog/Profile.html', context)


def demo(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/demo.html', context)


@login_required
def SendMessage(request):
	to_user = request.POST.get('to_user')
	body = request.POST.get('body')
	from_user = request.POST.get('from_user')

	
	Message.send_message(from_user, to_user, body)
	return redirect('/blog/')


@login_required
def contact(request,senderid,recipientid):
    messages = Message.get_messages(user=request.user)
    i = 0
    for message in messages:
        if message.is_read == False:
            i = i + 1
    users = get_all_users()
    recipient = users[0]
    sender = users[0]
    for user in users:
        if recipientid == user.id:
            recipient = user
        if senderid == user.id:
            sender = user
        
    context = {
        'recipient': recipient.user,
        'users': users,
        'sender': sender.user,
        'posts': Post.objects.all(), 
        'unread': i
    }
    return render(request, 'blog/contact.html', context)

#@login_required
#def contact(request,id):
#    logged_in = get_all_logged_in_users()
#    from_user = request.user
#    receiver = logged_in[0]
#    for user in logged_in:
#        if id == user.id:
#            receiver = user
#            break
#	to_user = User.objects.get(username=to_user_username)
#	Message.send_message(from_user, to_user, body)
#
#    context = {
#        'from_user': from_user,
#        'to_user': receiver.user,
#    }
#    return render(request, 'blog/contact.html', context)

@login_required
def inbox(request):
    messages = Message.get_messages(user=request.user)
    users = get_all_users()
    i = 0
    for message in messages:
        if message.is_read == False:
            i = i + 1
    messages.update(is_read=True)
    context = {
        'messages': messages, 
        'users': users,
        'unread':i
    }
    return render(request, 'blog/inbox.html', context)
