from django.urls import path

from blog import views
from blog.views import blog_list, BlogPagination
# from rest_framework.routers import DefaultRouter
#
urlpatterns = [
    path(r'list/', views.blog_list.as_view({'get': 'list'})),
    path(r'category/<str:slug>/', views.BlogPagination.as_view(), name='list'),
]

# router = DefaultRouter()
# router.register(r'list', blog_list, basename='list')
# router.register(r'^category/<str:slug>', blog_pagination, basename='list')
# urlpatterns = outer.urlsr
