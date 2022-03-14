from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import CategorySerializer, StorySerializer, ReplySerializer, ReplyCommentSerializer
from .models import Story, Category, Reply, ReplyComment

# Create your views here.

@csrf_exempt
@api_view(['GET'])
def get_content_blog(request, **kwargs):
    return Response({
        'ok': True,
        'data': {
            'title': "hiep"
        }
    })

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
        print(data)
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

@csrf_exempt
@api_view(['POST'])
def create_post(request, **kwargs):
    # user = request.user
    # if not user.is_authenticated:
    #     return Response({
    #         'ok': False,
    #         'msg': 'ban chua dan nhap'
    #     })
    data = request.data
    print(data)
    content = data.get('content', '')
    title = data.get('title', '')
    category = data.get('category', '')
    return Response({
        'ok': True
    })
