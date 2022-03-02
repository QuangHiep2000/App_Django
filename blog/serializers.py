from rest_framework import serializers
from blog.models import Blog, Category, BlogLike


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'slug', 'content', 'created_at', 'updated_at', 'is_public', 'is_removed', 'total_likes']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']


class BlogLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogLike
        fields = ['user', 'blog', 'created_at']

# class Blog_PaginationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Blog
#         fields = ['title', 'slug', 'content', 'created_at', 'updated_at', 'is_public', 'is_removed', 'name']
    # title = serializers.CharField(max_length=200, null=True)
    # slug = serializers.CharField(null=True)
    # content = serializers.CharField(null=True)
    # created_at = serializers.DateTimeField(auto_now_add=True)
    # updated_at = serializers.DateTimeField(auto_now=True)
    # is_public = serializers.BooleanField(default=False)
    # is_removed = serializers.BooleanField(default=False)
    #
    # def create(self, validated_data):
    #     return Blog.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.slug = validated_data.get('slug', instance.slug)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.created_at = validated_data.get('created_at', instance.created_at)
    #     instance.updated_at = validated_data.get('updated_at', instance.updated_at)
    #     instance.is_public = validated_data.get('is_public', instance.is_public)
    #     instance.is_removed = validated_data.get('is_removed', instance.is_removed)
    #     instance.save()
    #     return instance
