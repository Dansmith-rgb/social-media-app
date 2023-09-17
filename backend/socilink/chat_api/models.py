from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class ChatRoom(models.Model):
    name = models.CharField(max_length=100)
    admins = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    participants = models.ForeignKey(User, on_delete=models.CASCADE)
    chatroom_identifier = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(blank=True, upload_to="../media/uploads/profile_pictures", null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content