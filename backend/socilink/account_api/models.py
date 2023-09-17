from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.add(instance.profile)
        user_profile.save()


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    follows = models.ManyToManyField("self", related_name="followed_by", symmetrical=False, blank=True)
    profile_img = models.ImageField(blank=True, upload_to="../media/uploads/profile_pictures", default="../media/uploads/profile_pictures/default.png")
    bio = models.CharField(max_length=200, null=True, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    visibility = (
        ('pr', 'private'),
        ('pu', 'public')
    )
    access = models.CharField(max_length=2,choices=visibility, default='pr', null=True)

    def __str__(self):
        return self.user.username
    
class FriendRequest(models.Model):
    """
    Model to create a friend request if profile access is private
    """
    STATUS = (
        ('pe', 'Pending'),
        ('ac', 'Accepted'),
        ('de', 'Declined')
    )
    status = models.CharField(max_length=2, choices=STATUS)
    sent_at = models.DateTimeField(auto_now_add=True)
    from_user = models.ForeignKey(User, related_name="from_user", on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name="to_user", on_delete=models.CASCADE)
