from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver


class Message(models.Model):
	from_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='from_user')
	to_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='to_user')
	body = models.TextField(max_length=280, blank=True, null=True)
	is_read = models.BooleanField(default=False)

	def send_message(from_user, to_user, body):
		message = Message(
			from_user=from_user,
			to_user=to_user,
			body=body,
			is_read=False)
		message.save()

		return message

	def get_messages(user):
		messages = Message.objects.filter(to_user=user)
		return messages
