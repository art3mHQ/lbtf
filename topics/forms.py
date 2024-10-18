from django import forms

from .models import Topic


class TopicModelForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = (
            "title",
            "description",
            "topic_image",
            "attending_type",
            "nuber_of_participants",
        )
