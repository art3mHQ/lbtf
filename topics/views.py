import json
import os
from datetime import datetime

from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from profiles.models import Profile

from .models import Comment
from .models import Field
from .models import JoinRequest
from .models import Lang
from .models import Like
from .models import MyCustomTimeZones
from .models import Subfield
from .models import Topic
from .serializers import CommentSerializer
from .serializers import TopicSerializer

# def create_update_view(request):
#     langs = Lang.objects.all()

#     context = {
#     'langs': langs,
#     }
#     return render(request, 'topics/create.html', context)

# class TopicViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     # queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = TopicSerializer
#     permission_classes = [permissions.IsAuthenticated]


@api_view(["POST"])
def add_topic_api(request):
    serializer = TopicSerializer(data=request.data)
    topic_starter = Profile.objects.get(user=request.user)
    # print(serializer)
    if serializer.is_valid():
        ntop = serializer.save(poster=topic_starter)
        # print(ntop.id)
        # ntop['id'] = ntop.id
        # TODO add a success message

        messages.success(request, "Topic creation successful")
        return JsonResponse(ntop.id, status=201, safe=False)
    return JsonResponse(serializer.errors, status=400)


@api_view(["PUT"])
def update_topic_api(request, pk):
    try:
        topic_object = Topic.objects.get(pk=pk)
    except Topic.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "PUT":
        # parsed_data = JSONParser().parse(request)
        serializer = TopicSerializer(topic_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            messages.success(request, "Topic updated successfully")
            return JsonResponse(topic_object.id, status=200, safe=False)
        return JsonResponse(serializer.errors, status=400)
    return None


@api_view(["POST"])
def add_comment_api(request):
    serializer = CommentSerializer(data=request.data)
    comment_starter = Profile.objects.get(user=request.user)
    # print(serializer)
    if serializer.is_valid():
        comment_poster = serializer.save(user=comment_starter)
        # print(ntop.id)
        # ntop['id'] = ntop.id
        # TODO add a success message

        messages.success(request, "Comment creation successful")
        return JsonResponse(comment_poster.id, status=201, safe=False)
    return JsonResponse(serializer.errors, status=400)


# upload picture (or video) to server on change
class FileUploadView(APIView):
    parser_classes = (FileUploadParser,)

    def put(self, request, filename, format=None):
        user = self.request.user
        if not user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        # print('wowawewa222!!!!!!')
        up_file = request.FILES["file"]
        # print(up_file)

        t = datetime.today()
        filename = f'{settings.MEDIA_ROOT+"/topics"}/{t.year}/{t.month:02d}/{t.day:02d}/{up_file.name}'
        os.makedirs(os.path.dirname(filename), exist_ok=True)  # create dir
        destination = open(filename, "wb+")
        for chunk in up_file.chunks():
            destination.write(chunk)
        destination.close()  # File should be closed only after all chuns are added
        # print(destination.name)
        resptosend = {}
        # resptosend['file_url'] = str(settings.MEDIA_ROOT + '/Video/' + up_file.name)
        filename_kinda_url = (
            f"/topics/{t.year}/{t.month:02d}/{t.day:02d}/{up_file.name}"
        )
        # resptosend['file_url'] = filename
        resptosend["file_url"] = filename_kinda_url

        return Response(resptosend, status=status.HTTP_201_CREATED)


def main_page_view(request):
    qs = Topic.objects.all()[:10]
    context = {
        "qs": qs,
    }
    return render(request, "topics/mainpage/home.html", context)


class TopicDetailView(DetailView):
    model = Topic
    context_object_name = "topic"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        user = self.request.user
        context = super().get_context_data(**kwargs)
        # check if user not anaminous
        if user.is_authenticated:
            # Add in a QuerySet of all the books
            context["profile"] = Profile.objects.get(user=user)
        context["comments"] = Comment.objects.filter(topic=self.object).order_by(
            "-updated",
        )
        context["requests"] = JoinRequest.objects.filter(topic=self.object).order_by(
            "-updated",
        )
        print(context["comments"])
        return context


def like_unlike_topic_ajax(request):
    user = request.user

    if request.method == "POST":
        # print('fffffff_2')
        topic_id = json.load(request)["topic_id"]
        # print(topic_id)

        # this consist of 2 steps
        # topic_id = request.POST.get('topic_id')

        topic_object = Topic.objects.get(id=topic_id)
        profile = Profile.objects.get(user=user)

        # Step one change liked value in Topic model

        if profile in topic_object.liked.all():
            topic_object.liked.remove(profile)
        else:
            topic_object.liked.add(profile)

        print(topic_object.liked.all().count())
        print("_____1_number_oflike__________________")

        # Step 2 get value or create like

        like, created = Like.objects.get_or_create(user=profile, topic_id=topic_id)

        if not created:
            if like.value == "Like":
                like.value = "Unlike"
                pluslike = -1  # value for passing to front
            else:
                like.value = "Like"
                pluslike = 1
                # print(like.value)
                # print('_____likeee_2___________________')
        else:
            like.value = "Like"
            pluslike = 1

        topic_object.save()
        like.save()

        data = {
            "value": pluslike,
            "count": topic_object.liked.all().count(),
        }
        return JsonResponse(data)
    return redirect()


class TopicCreateView(CreateView):
    model = Topic
    template_name = "topics/create.html"
    fields = [
        "title",
        "description",
        "topic_image",
        "location_country",
        # 'location_region',
        # 'location_city',
        "attending_type",
        "nuber_of_participants",
    ]

    def get_context_data(self, **kwargs):
        context = super(TopicCreateView, self).get_context_data(**kwargs)
        # context['select_cat'] = cat    # добавленно (для совместимости шаблонов)
        context["fieldset"] = Field.objects.order_by("name")
        context["langs"] = Lang.objects.all()
        context["timezones"] = MyCustomTimeZones.objects.all()
        return context

    def form_valid(self, form):
        form.instance.poster = self.request.user
        return super().form_valid(form)


class TopicUpdateView(UpdateView):
    model = Topic
    template_name = "topics/create.html"
    fields = [
        "title",
        "description",
        "topic_image",
        "location_country",
        # 'location_region',
        # 'location_city',
        "attending_type",
        "nuber_of_participants",
    ]

    def get_context_data(self, **kwargs):
        # TODO add odjects subfield context for better representation (displaing sublields onload)
        context = super(TopicUpdateView, self).get_context_data(**kwargs)
        # context['select_cat'] = cat    # добавленно (для совместимости шаблонов)
        context["fieldset"] = Field.objects.order_by("name")
        context["langs"] = Lang.objects.all()
        context["timezones"] = MyCustomTimeZones.objects.all()
        return context

    def form_valid(self, form):
        form.instance.poster = self.request.user
        return super().form_valid(form)


def get_subfield_list(request, *args, **kwargs):
    selected_field = kwargs.get("id")
    subfield_ls = list(
        Subfield.objects.filter(parent_field__pk=selected_field).values("id", "name"),
    )
    return JsonResponse({"data": subfield_ls})


# def index(request):
#     return render(request, 'topics/topic.html')

# def detail(request, topic_id):
#     return HttpResponse("You're looking at topic %s." % topic_id)

# def createtopic(request):
#     return render(request, 'topics/create.html')
