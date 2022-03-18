from django.urls import path
from forum import views
# from blog.views import BlogPagination
# from rest_framework.routers import DefaultRouter
#
app_name = "forum"

urlpatterns = [
    # path('create-post/', views.create_post, name='create_post'),
    path('create-post/', views.CreatePOST.as_view(), name='create_post'),
    path('update-post/', views.UpdatePOST.as_view(), name='update_post'),
    path('api/list-story/', views.StoryListAPIView.as_view(), name='api_list_story'),
    path('api/add-story-like/', views.AddLikeAPI.as_view(), name='api_add_story_like'),
    path('api/story-detail/', views.APIStoryDetail.as_view(), name='api_story_detail'),
    path('api/delete-story/', views.APIDeleteStory.as_view(), name='api_delete_story'),
    # path('api/list-comment/', views.APIListComment.as_view(), name='list_comment'),
    path('api/add-reply/', views.APIAddReply.as_view(), name='api_add_reply'),
    path('api/edit-reply/', views.APIEditReply.as_view(), name='api_edit_reply'),
]
