# from cities_light.models import City
from cities_light.models import Country

# from cities_light.models import Region
# from django.conf import settings
# from django.conf.global_settings import LANGUAGES
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone

from profiles.models import Profile

# Field (Subfield & Customfield) means field of humam knowledge and occupation


class Lang(models.Model):
    ticker = models.CharField(max_length=3)
    name = models.CharField(max_length=36)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


# Table MyCustomTimeZones was created by dumping pyts zones by pytz.common_timezones
# then pasting in postgress
class MyCustomTimeZones(models.Model):
    timezone_char = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.timezone_char}"

    # def __str__(self):
    # # Return the modified output
    # modified_output = self.modify_field_name()
    # return modified_output

    def get_original_field(self):
        # Return the original field value without modification
        return self.timezone_char

    def modified_truncked_zone(self):
        # Modify the field output here
        orig_str = self.get_original_field()
        return orig_str[orig_str.rfind("/") + 1 :]  # leave just city from timezone


class Field(models.Model):
    name = models.CharField(max_length=26)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Subfield(models.Model):
    name = models.CharField(max_length=36)
    parent_field = models.ManyToManyField(Field, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Customfield(models.Model):
    name = models.CharField(max_length=36)
    parent_field = models.ForeignKey(
        Field,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


ATTEND_CHOISES = (
    ("O", "online"),
    ("P", "offline"),
    ("M", "on+offline"),
)

SCHEDULE_FREQUENCY = (
    ("1", "once a week"),
    ("2", "twice a week"),
    ("3", "3 times a week"),
    ("4", "4 times a week"),
    ("5", "5 times a week"),
    ("6", "6 times a week"),
    ("7", "7 times a week"),
    ("C", "custom"),
)

# class TopicFollowers


class Topic(models.Model):
    title = models.CharField(max_length=110)
    poster = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name="topics")
    description = models.TextField(max_length=900)
    date_posted = models.DateTimeField(default=timezone.now)
    topic_image = models.ImageField(
        default="no_image.jpg",
        upload_to="topics/%Y/%m/%d/",
        validators=[FileExtensionValidator(["png", "jpg", "jpeg"])],
        blank=True,
        null=True,
        verbose_name="topic img",
    )
    # sci_categoty = models.ForeignKey(Category, on_delete=models.PROTECT)
    location = models.CharField(max_length=110, blank=True)
    # location_city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    location_country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    # location_region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True)
    time_zone = models.ForeignKey(
        MyCustomTimeZones,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    attending_type = models.CharField(choices=ATTEND_CHOISES, max_length=1, default="M")
    nuber_of_participants = models.PositiveSmallIntegerField(
        default=2,
        verbose_name="Max Number of Participants",
    )
    language = models.ForeignKey(Lang, on_delete=models.CASCADE, blank=True, null=True)
    # language = models.CharField(max_length=60, blank=True, null=True)
    # requestes_to_join = models.ForeignKey(, on_delete=models.PROTECT, blank=True)
    # comments = models.ForeignKey(Comments, on_delete=models.PROTECT)
    schedule_freq = models.CharField(
        choices=SCHEDULE_FREQUENCY,
        max_length=1,
        default="C",
        verbose_name="Schedule",
    )
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(
        Profile,
        blank=True,
        related_name="likes",
    )  # related_name="likes" for reverse only
    field = models.ForeignKey(Field, on_delete=models.CASCADE, blank=True, null=True)
    subfield = models.ForeignKey(
        Subfield,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    # custom_field = models.ForeignKey(Customfield, on_delete=models.PROTECT, blank=True, null=True)
    custom_field = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return f"{self.title[:28]} by {self.poster}- #{self.pk}"

    def get_absolute_url(self):
        return reverse("topics:topic_detail", kwargs={"pk": self.pk})

    def num_likes(self):
        return self.liked.all().count()

    def num_comments(self):
        return self.comment_set.all().count()

    def num_requests(self):
        return self.joinrequest_set.all().count()

    def num_accepted_requests(self):
        return self.joinrequest_set.filter(approved=True).count()


class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.PROTECT)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    body = models.TextField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}-{self.topic}-{self.body}"


class JoinRequest(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    approve_time = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.topic}-{self.user}-"


LIKE_CHOICES = (
    ("Like", "Like"),
    ("Unlike", "Unlike"),
)


class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}-{self.topic}-{self.value}"
