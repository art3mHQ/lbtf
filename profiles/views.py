import json

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from topics.models import Topic

from .forms import ProfileModelForm
from .models import Profile


def my_profile_view(request):
    obj = Profile.objects.get(user=request.user)
    qs = Topic.objects.filter(poster=obj)

    context = {
        "object": obj,
        "qs": qs,
    }

    return render(request, "profiles/myprofile.html", context)


def profile_view(request, profile_id):
    obj = get_object_or_404(Profile, pk=profile_id)
    qs = Topic.objects.filter(poster=obj)

    context = {
        "object": obj,
        "qs": qs,
    }

    return render(request, "profiles/myprofile.html", context)


def my_profile_edit_view(request):
    obj = Profile.objects.get(user=request.user)
    form = ProfileModelForm(request.POST or None, request.FILES or None, instance=obj)
    confirm = False
    if request.method == "POST":
        if form.is_valid():
            form.save()
            confirm = True
    context = {
        "object": obj,
        "form": form,
        "confirm": confirm,
    }

    return render(request, "profiles/myprofile_edit.html", context)


def followers(request, profile_id):
    obj = get_object_or_404(Profile, pk=profile_id)
    id_set = obj.get_friends()
    qs = Profile.objects.filter(user__in=id_set)

    print(id_set)
    print("__id_set__")

    context = {
        "object": obj,
        "qs": qs,
    }

    return render(request, "profiles/followers-list.html", context)


def following(request, profile_id):
    obj = get_object_or_404(Profile, pk=profile_id)
    id_set = obj.followed_users.all()
    qs = Profile.objects.filter(user__in=id_set)

    # print(id_set)
    # print('__id_set__')

    context = {
        "object": obj,
        "qs": qs,
    }
    return render(request, "profiles/following.html", context)


def follow_unfollow_ajax(request):
    user = request.user

    if request.method == "POST":
        # print('fffffff_2')
        user_to_follow_id = json.load(request)["user_id"]
        print(user_to_follow_id)
        print("user_to_follow_id")
        print(user)
        print(user.name)
        print("user")
        # this consist of 2 steps
        # topic_id = request.POST.get('topic_id')

        user_to_follow_object = get_user_model().objects.get(id=user_to_follow_id)
        profile_to_follow = Profile.objects.get(user=user_to_follow_object)

        follower_profile = Profile.objects.get(user=user)

        # Step one change friends list in model

        if user in profile_to_follow.friends.all():
            profile_to_follow.friends.remove(user)
            follower_profile.followed_users.remove(user_to_follow_object)
            plusfollow = -1
        else:
            profile_to_follow.friends.add(user)
            follower_profile.followed_users.add(user_to_follow_object)
            plusfollow = 1

        print(profile_to_follow.get_friends_no())
        print(profile_to_follow.user.name)
        print(profile_to_follow.user)
        print("_____number_of_followers__________________")

        # Step 2 get value or create like

        data = {
            "value": plusfollow,
            "count": profile_to_follow.friends.all().count(),
        }
        return JsonResponse(data)

    return redirect()
