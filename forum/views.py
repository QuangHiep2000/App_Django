from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import CategorySerializer, StorySerializer, ReplySerializer, ReplyCommentSerializer, StoryLikeSerializer
from .models import Story, Category, Reply, ReplyComment, StoryLike


# Create your views here.

# class CreatePOST(ListAPIView):
#     serializer_class = StorySerializer
#     permission_classes = [AllowAny]
#
#     def get_queryset(self):
#         story = Story.objects.filter(id=2)
#         return story


class CreatePOST(ListCreateAPIView):
    serializer_class = StorySerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return Response({
                'ok': False,
                'msg': 'ban chua dan nhap'
            })
        data = self.request.data
        content = data.get('content', '')
        title = data.get('title', '')
        category = data.get('category', '')
        last_activity_by = data.get('last_activity_by', '')
        status = data.get('status', '')
        num_participants = data.get('num_participants', '')
        ip_address = data.get('ip_address', '')
        user_agent = data.get('user_agent', '')
        # user = data.get('user', '')
        # _user = User.objects.get(id=user)
        try:
            _category = Category.objects.get(name=category)
            _last_activity_by = User.objects.get(id=last_activity_by)
        except Category.DoesNotExist:
            return []
        story = Story.objects.create(
            # user=_user,
            content=content,
            title=title,
            last_activity_by=_last_activity_by,
            status=status,
            num_participants=num_participants,
            ip_address=ip_address,
            user_agent=user_agent,
        )
        story.category.add(_category)
        return Response({
            'ok': True
        })


class UpdatePOST(ListCreateAPIView):
    serializer_class = StorySerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return Response({
                'ok': False,
                'msg': 'ban chua dan nhap'
            })
        data = self.request.data
        content = data.get('content', '')
        title = data.get('title', '')
        category = data.get('category', '')
        code = data.get('code', '')
        # user = data.get('user', '')
        # _user = User.objects.get(id=user)

        if Story.objects.filter(
            user=user
        ).exists():
            try:
                _story = Story.objects.get(code=code)
                print(_story)
            except Story.DoesNotExist:
                return Response({
                    'ok': False
                })
            try:
                _category = Category.objects.get(name=category)
            except Category.DoesNotExist:
                return Response({
                    'ok': False
                })

            Story.objects.filter(code=code).update(
                # user=_user,
                content=content,
                title=title,
            )

            _story.category.add(_category)
            category_will_delete = Category.objects.filter().exclude(id=_category.id)
            for i in category_will_delete:
                temp = Category.objects.get(id=i.id)
                _story.category.remove(temp)

            return Response({
                'ok': True
            })

        else:
            return Response({
                'ok': False
            })


class ListPagination(PageNumberPagination):
    # serializer_class = StorySerializer
    # permission_classes = [AllowAny]
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 20

    def get_paginated_response(self, data):
        return Response({
            'nulItems': self.page.paginator.count,
            'totalPages': self.page.paginator.num_pages,
            'pageSize': self.page_size,
            'currentPage': self.page.number,
            'items': data,
        })

class StoryListAPIView(ListAPIView):
    serializer_class = StorySerializer
    permission_classes = [AllowAny]
    pagination_class = ListPagination

    def get_queryset(self):
        list_story = Story.objects.filter(status='P').order_by('-updated_at')
        return list_story


class AddLikeAPI(ListCreateAPIView):
    serializer_class = StorySerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        user = request.user
        data = self.request.data
        code = data.get('code', '')
        if not user.is_authenticated:
            return Response({
                'ok': False,
                'msg': 'ban chua dan nhap'
            })
        try:
            story = Story.objects.get(code=code)
        except Story.DoesNotExist:
            return Response({
                'ok': False
            })
        StoryLike.objects.create(
            user=user,
            story=story
        )
        return Response({
            'ok': True
        })



