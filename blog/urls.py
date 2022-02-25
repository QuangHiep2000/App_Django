from django.urls import path

from blog import views
# from blog.views import BlogPagination
# from rest_framework.routers import DefaultRouter
#
app_name = "blog"

urlpatterns = [
    path('list/', views.blog_list, name='list'),
    path('category/<str:slug>/', views.CategoryPagination.as_view()),
    path('', views.AdminPage.as_view()),
    path('blog/blog-<str:slug>', views.BlogSlug.as_view()),
    path('blog/blog-<str:slug>/content', views.get_content_blog, name='api_blog'),
]

# router = DefaultRouter()
# router.register(r'list', blog_list, basename='list')
# router.register(r'^category/<str:slug>', blog_pagination, basename='list')
# urlpatterns = outer.urlsr
