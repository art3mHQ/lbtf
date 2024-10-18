from django.urls import path

from .views import follow_unfollow_ajax
from .views import followers
from .views import following
from .views import my_profile_edit_view
from .views import my_profile_view
from .views import profile_view

app_name = "profiles"

urlpatterns = [
    path("myprofile/", my_profile_view, name="my-profile-view"),
    path("<int:profile_id>/", profile_view, name="profile-view"),
    path("myprofile/~edit/", my_profile_edit_view, name="my-profile-edit-view"),
    path("follow/", follow_unfollow_ajax, name="follow-unfollow-ajax"),
    path("followers-list/<int:profile_id>/", followers, name="followers-view"),
    path("following/<int:profile_id>/", following, name="following-view"),
    # path('following-list/', following, name='following-view'),
]
