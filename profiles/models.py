import random
import string

from django.conf import settings
from django.db import models
from slugify import slugify


class Profile(models.Model):
    first_name = models.CharField(max_length=200, blank=True)  # maybe OneToOne
    last_name = models.CharField(max_length=200, blank=True)  # maybe OneToOne
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(default="no bio...", max_length=500, blank=True)
    email = models.EmailField(max_length=200, blank=True)  # maybe OneToOne
    country = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(
        default="avatar.png",
        upload_to="avatars/%Y/%m/%d/",
        blank=True,
    )
    # didn't want to change friends for followers so actually friends are followers here
    friends = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name="friends",
    )
    # people who this account follow (aka following)
    followed_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name="following",
    )
    slug = models.SlugField(unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}-{self.created.strftime('%d-%m-%Y')}"

    __initial_first_name = None
    __initial_last_name = None

    def save(self, *args, **kwargs):
        ex = False
        to_slug = self.slug
        if (
            self.first_name != self.__initial_first_name
            or self.last_name != self.__initial_last_name
            or self.slug == ""
        ):
            if self.first_name and self.last_name:
                to_slug = slugify(str(self.first_name) + str(self.last_name))
                ex = Profile.objects.filter(slug=to_slug).exists()
                while ex:
                    # random sufix if slug equals first+last name
                    letters = string.ascii_letters
                    to_slug = slugify(
                        to_slug
                        + " "
                        + "".join(random.choice(letters) for i in range(5)),
                    )
                    ex = Profile.objects.filter(slug=to_slug).exists()
            else:
                to_slug = str(self.user)
        self.slug = to_slug
        super().save(*args, **kwargs)

    def get_friends(self):
        return self.friends.all()

    def get_friends_no(self):
        return self.friends.all().count()

    def get_following_no(self):
        return self.followed_users.all().count()

    def get_posts_no(self):
        return self.topics.all().count()

    def get_all_authors_posts(self):
        return self.topics.all()

    def get_likes_given_no(self):
        likes = self.like_set.all()
        total_liked = 0
        for item in likes:
            if item.value == "Like":
                total_liked += 1
        return total_liked

    def get_likes_recieved_no(self):
        posts = self.topics.all()
        total_liked = 0
        for item in posts:
            total_liked += item.liked.all().count()
        return total_liked


STATUS_CHOICES = (
    ("s", "send"),
    ("a", "accepted"),
)

# class RelationshipManager(models.Manager):
#     def invatations_received(self, receiver):
#         qs = Relationship.objects.filter(receiver=receiver, status='send')
#         return qs


class RelationshipManager(models.Manager):
    def invitation_receved(self, receiver):
        qs = Relationship.objects.filter(receiver=receiver, status="s")
        return qs


class Relationship(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="receiver",
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = RelationshipManager()

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"
