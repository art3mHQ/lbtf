from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile
from .models import Relationship


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def post_save_create_profile(sender, instance, created, **kwargs):
    # print('sender', sender)
    # print('instance', instance)
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Relationship)
def post_save_add_to_friends(sender, instance, created, **kwargs):
    sender_ = instance.sender
    receiver_ = instance.receiver
    if instance.status == "a":
        sender_.friends.add(receiver_.user)
        receiver_.friends.add(sender_.user)
        sender_.save()
        receiver_.save()


# @receiver(pre_delete, sender=Relationship)
# def pre_delete_remove_from_friends(sender, instance, **kwargs):
#     sender = instance.sender
#     receiver = instance.receiver
#     sender.friends.remove(receiver.user)
#     receiver.friends.remove(sender.user)
#     sender.save()
#     receiver.save()
