from django.db.migrations import serializer
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.authtoken.admin import User

from .models import Category, Story, Reply, ReplyComment, StoryLike


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'id']


# class SubCommentSerializer(serializers.Serializer):
#     sub_comments = serializers.SerializerMethodField()
#     class Meta:
#         fields = ['sub_comments']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'slug',
            'desc_safe',
            'order',
            'color_code',
        ]


class StorySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Story
        fields = [
            'code',
            'user',
            'content',
            'content_safe',
            'title',
            'category',
            'last_activity_by',
            'last_activity_at',
            'created_at',
            'updated_at',
            'scheduled_at',
            'published_at',
            'STORY_STATUS_CHOICES',
            'status',
            'closed',
            'featured_until',
            'featured',
            'edited_at',
            'edited_by',
            'num_views',
            'num_likes',
            'num_replies',
            'num_comments',
            'num_participants',
            'ip_address',
            'user_agent',
        ]


class ReplySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    sub_comments = serializers.SerializerMethodField()
    num_reply_comments = serializers.SerializerMethodField()

    class Meta:
        model = Reply
        fields = [
            'user',
            'reply_order',
            'content',
            'content_safe',
            'removed',
            'created_at',
            'updated_at',
            # 'ip_address',
            'user_agent',
            # 'edited_at',
            # 'edited_by',
            'sub_comments',
            'num_reply_comments',
        ]

    def get_sub_comments(self, obj):
        list = []
        for x in obj['sub_comments']:
            list.append({
                'Content': x.content,
                'user': UserSerializer(x.user).data,
            })
        return {
            'data': list
        }

    def get_num_reply_comments(self, obj):
        return obj['num_reply_comments']


class ReplyCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ReplyComment
        fields = [
            'user',
            'reply',
            'content',
            'mention_to',
            'removed',
            'ip_address',
            'user_agent',
        ]


class StoryLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryLike
        fields = [
            'user',
            'story',
            'created_at',
        ]




