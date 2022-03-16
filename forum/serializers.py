from rest_framework import serializers
from .models import Category, Story, Reply, ReplyComment, StoryLike


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
    class Meta:
        model = Reply
        fields = [
            'user',
            'story',
            'reply_order',
            'content',
            'content_safe',
            'removed',
            'created_at',
            'updated_at',
            'ip_address',
            'user_agent',
            'edited_at',
            'edited_by',
        ]


class ReplyCommentSerializer(serializers.ModelSerializer):
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
