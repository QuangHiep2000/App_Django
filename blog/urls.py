from django.urls import path

from blog import views
# from blog.views import BlogPagination
# from rest_framework.routers import DefaultRouter
#
app_name = "blog"

urlpatterns = [
    path('', views.AdminPage.as_view()),
    path('list/', views.blog_list, name='list'),
    path('category/<str:slug>/', views.CategoryPagination.as_view()),
    path('blog/blog-<str:slug>', views.BlogSlug.as_view(), name='blog_slug'),
    path('blog/blog-<str:slug>/content', views.get_content_blog, name='api_blog'),
    path('login/', views.BlogLogin.as_view(), name='login'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('logout/', views.logout_page, name='logout'),
]

# router = DefaultRouter()
# router.register(r'list', blog_list, basename='list')
# router.register(r'^category/<str:slug>', blog_pagination, basename='list')
# urlpatterns = outer.urlsr
