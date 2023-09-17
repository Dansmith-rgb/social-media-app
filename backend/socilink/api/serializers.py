from rest_framework import serializers
from .models import Profile, Notification, FriendRequest, Post, Comment
from django.contrib.auth.models import User

class ProfileSerializer(serializers.Serializer):
    class Meta:
        model = Profile
        fields = '__all__'
        depth=1

class NotificationSerializer(serializers.Serializer):
    class Meta:
        model = Notification
        fields = '__all__'
        depth=1