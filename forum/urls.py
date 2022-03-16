from django.urls import path
from forum import views
# from blog.views import BlogPagination
# from rest_framework.routers import DefaultRouter
#
app_name = "forum"

urlpatterns = [
    # path('create-post/', views.create_post, name='create_post'),
    path('create-post/', views.CreatePOST.as_view(), name='create_post'),
    path('update-post/', views.UpdatePOST.as_view(), name='update_post')
]