from rest_framework import serializers

from .models import Comment
from .models import JoinRequest
from .models import Topic


class TopicSerializer(serializers.ModelSerializer):
    topic_image = serializers.CharField(allow_blank=True, max_length=200, default=None)

    class Meta:
        model = Topic
        fields = [
            "title",
            "description",
            "location",
            "time_zone",
            "topic_image",
            "attending_type",
            "nuber_of_participants",
            "language",
            "schedule_freq",
            "field",
            "subfield",
            "custom_field",
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "topic",
            "body",
        ]


class JoinRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinRequest
        fields = [
            "topic",
        ]


class AproveJoinRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinRequest
        fields = [
            "topic",
            "approved",
        ]


# class CartSerializer(serializers.Serializer):

#     primary_id = serializers.IntegerField()
#     added_stems = serializers.BooleanField(default=False)
#     secondary_id = serializers.IntegerField(default=0)
#     name = serializers.CharField(max_length=50)
#     address = serializers.CharField(max_length=250)
#     rec_phone_number = serializers.CharField(max_length=16)
#     delivery_date = serializers.DateTimeField()
#     delivery_time = serializers.TimeField()
#     delivery_time_till = serializers.TimeField()

#     card_id = serializers.IntegerField(default=0)

#     card_inscript_from = serializers.CharField(allow_blank=True, max_length=50, default=None)
#     card_inscript_to = serializers.CharField(allow_blank=True, max_length=50, default=None)
#     card_inscript_text = serializers.CharField(allow_blank=True, max_length=350, default=None)
#     given_price = serializers.DecimalField(max_digits=8, decimal_places=2, default=None)
#     credit_discount = serializers.DecimalField(max_digits=8, decimal_places=2, default=None)
#     # video = serializers.FilePathField(path=settings.MEDIA_ROOT, match=None, recursive=True, allow_folders=True, default=None)
#     video = serializers.CharField(allow_blank=True, max_length=200, default=None)


#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Product.objects.create(**validated_data)
