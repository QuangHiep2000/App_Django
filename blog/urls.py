from django.urls import path

from blog import views
# from blog.views import BlogPagination
# from rest_framework.routers import DefaultRouter
#
# app_name = "blog"

urlpatterns = [
    path(r'list/', views.blog_list),
    path(r'category/<str:slug>/', views.CategoryPagination.as_view()),
    path(r'', views.AdminPage.as_view())
]

# router = DefaultRouter()
# router.register(r'list', blog_list, basename='list')
# router.register(r'^category/<str:slug>', blog_pagination, basename='list')
# urlpatterns = outer.urlsr
