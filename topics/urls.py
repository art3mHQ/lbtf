from django.urls import path

from . import views
from .views import TopicCreateView
from .views import TopicDetailView
from .views import TopicUpdateView
from .views import get_subfield_list
from .views import like_unlike_topic_ajax

app_name = "topics"

urlpatterns = [
    # path('create/', create_update_view, name='create_update_view'),
    path("create/", TopicCreateView.as_view(), name="create_update_view"),
    # ex: /topics/5/
    path("<int:pk>/", TopicDetailView.as_view(), name="topic_detail"),
    path("<int:pk>/update", TopicUpdateView.as_view(), name="update_view_topic"),
    path("create/subfld-json/<int:id>/", get_subfield_list, name="subfld-json"),
    path("like/", like_unlike_topic_ajax, name="like-topic-json"),
    path("add_topic_api/", views.add_topic_api, name="add_topic_api"),
    path("add_topic_api/<int:pk>", views.update_topic_api, name="update_topic_api"),
    path("add_comment/", views.add_comment_api, name="add_comment_api"),
    path(
        "upload/<str:filename>",
        views.FileUploadView.as_view(),
        name="add_topic_photo",
    ),
]
