from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, ListCreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import CategorySerializer, StorySerializer, ReplySerializer, ReplyCommentSerializer, \
    StoryLikeSerializer, UserSerializer
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


class APIStoryDetail(ListAPIView):
    serializer_class = StorySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        code = self.request.GET.get('code', '')
        if not code:
            return []
        story = Story.objects.filter(status='P', code=code).only(
            'code', 'content_safe', 'title', 'category', 'created_at',
            'num_views', 'num_likes', 'num_replies', 'num_comments', 'updated_at', 'user')
        if not story:
            return []
        return story


class APIDeleteStory(DestroyAPIView):
    serializer_class = StorySerializer
    permission_classes = [AllowAny]

    def delete(self, request, *args, **kwargs):
        user = request.user
        data = self.request.data
        code = data.get('code', '')
        if not user.is_authenticated:
            return Response({
                'ok': False,
                'msg': 'ban chua dan nhap'
            })

        try:
            story = Story.objects.get(code=code, user=user)
        except Story.DoesNotExist:
            return Response({
                'ok': False
            })

        story.delete()

        return Response({
            'ok': True
        })


class APIListComment(ListAPIView):
    serializer_class = ReplySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        code = self.request.GET.get('code', '')
        if not code:
            return []
        story = Story.objects.filter(code=code).first()
        if not story:
            return []
        reply = Reply.objects.select_related('user').filter(story=story)
        replies_id = [x.id for x in reply]
        data = []
        reply_comment = ReplyComment.objects.filter(reply_id__in=replies_id).order_by('-id')
        for x in reply:
            _reply_comment = [rc for rc in reply_comment if rc.reply_id == x.id]
            data.append({
                'user': x.user,
                'removed': x.removed,
                'content_safe': x.content_safe,
                'created_at': x.created_at,
                'sub_comments': _reply_comment[:3], # chỗ này lấy 3 bình luận con mới nhất, list of objects
                'num_reply_comments': len(_reply_comment),
            })
        return data


class APIAddReply(ListCreateAPIView):
    serializer_class = ReplySerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        user = self.request.user
        if not user.is_authenticated:
            return Response({
                'ok': False,
                'msg': 'ban chua dan nhap'
            })
        data = self.request.data
        code = data.get('code', '')
        content = data.get('content', '')
        try:
            story = Story.objects.get(code=code)
        except Story.DoesNotExist:
            return Response({
                'ok': False
            })
        Reply.objects.create(story=story, content=content, user=user)
        return Response({
            'ok': True
        })


class APIEditReply(ListCreateAPIView):
    serializer_class = ReplySerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        user = self.request.user
        if not user.is_authenticated:
            return Response({
                'ok': False,
                'msg': 'ban chua dan nhap'
            })
        data = self.request.data
        code = data.get('code', '')
        content = data.get('content', '')
        created_at = data.get('created_at', '')
        try:
            story = Story.objects.get(code=code)
        except Story.DoesNotExist:
            return Response({
                'ok': False
            })
        try:
            reply = Reply.objects.get(user=user, story=story, created_at=created_at)
        except Reply.DoesNotExist:
            return Response({
                'ok': False,
            })
        Reply.objects.filter(id=reply.id).update(content=content)
        print(reply)
        return Response({
            'ok': True
        })

class APIReplyComment(ListAPIView):
    serializer_class = ReplyCommentSerializer
    permission_classes = [AllowAny]
    pagination_class = ListPagination

    def get_queryset(self):
        reply = Reply.objects.filter(id=7).first()
        if not reply:
            return []
        replies_comments = ReplyComment.objects.filter(reply=reply.id)
        if not replies_comments:
            return []
        return replies_comments


class APIDeleteReply(DestroyAPIView):
    serializer_class = ReplySerializer
    permission_classes = [AllowAny]

    def delete(self, request, *args, **kwargs):
        user = request.user
        data = self.request.data
        reply_id = data.get('id', '')
        if not user.is_authenticated:
            return Response({
                'ok': False,
                'msg': 'ban chua dan nhap'
            })

        try:
            reply = ReplyComment.objects.get(id=reply_id, user=user)
        except Reply.DoesNotExist:
            return Response({
                'ok': False
            })

        reply.delete()

        return Response({
            'ok': True
        })


class APIAddReplyComment(ListCreateAPIView):
    serializer_class = ReplyCommentSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        user = self.request.user
        if not user.is_authenticated:
            return Response({
                'ok': False,
                'msg': 'ban chua dan nhap'
            })
        data = self.request.data
        reply_id = data.get('id', '')
        content = data.get('content', '')
        try:
            reply = Reply.objects.get(id=reply_id)
        except Reply.DoesNotExist:
            return Response({
                'ok': False
            })
        ReplyComment.objects.create(reply=reply, content=content, user=user)
        return Response({
            'ok': True
        })

class APIUpdateReplyComment(UpdateAPIView):
    serializer_class = ReplyCommentSerializer
    permission_classes = [AllowAny]

    def update(self, request, *args, **kwargs):
        user = self.request.user
        if not user.is_authenticated:
            return Response({
                'ok': False,
                'msg': 'ban chua dan nhap'
            })
        data = self.request.data
        reply_comment_id = data.get('id', '')
        content = data.get('content', '')
        try:
            reply_comment = ReplyComment.objects.get(id=reply_comment_id)
        except ReplyComment.DoesNotExist:
            return Response({
                'ok': False
            })
        if reply_comment.user == user:
            reply_comment.content = content
            reply_comment.save()
            return Response({
                'ok': True
            })
