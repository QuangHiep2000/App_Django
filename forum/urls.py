from django.urls import path
from forum import views

app_name = "forum"

urlpatterns = [
    path('api/create-post/', views.CreatePOST.as_view(), name='create_post'),
    path('update-post/', views.UpdatePOST.as_view(), name='update_post'),
    path('api/list-story/', views.StoryListAPIView.as_view(), name='api_list_story'),
    path('api/add-story-like/', views.AddLikeAPI.as_view(), name='api_add_story_like'),
    path('api/story-detail/', views.APIStoryDetail.as_view(), name='api_story_detail'),
    path('api/delete-story/', views.APIDeleteStory.as_view(), name='api_delete_story'),
    path('api/list-comment/', views.APIListComment.as_view(), name='list_comment'),
    path('api/add-reply/', views.APIAddReply.as_view(), name='api_add_reply'),
    path('api/edit-reply/', views.APIEditReply.as_view(), name='api_edit_reply'),
    path('api/reply-comment/', views.APIReplyComment.as_view(), name='api_reply_comment'),
    path('api/delete-reply/', views.APIDeleteReply.as_view(), name='api_delete_reply'),
    path('api/add-reply-comment/', views.APIAddReplyComment.as_view(), name='add_reply_comment'),
    path('api/update-reply-comment/', views.APIUpdateReplyComment.as_view(), name='update_reply_comment'),
    path('api/delete-reply-comment/', views.APIDeleteReplyComment.as_view(), name='delete_reply_comment'),
    path('api/catefory/', views.APICategory.as_view(), name='api_catefory'),
]
