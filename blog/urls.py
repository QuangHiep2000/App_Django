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
    path('blog/blog-', views.get_content_blog, name='blog_slug_life_new'),
    path('login/', views.BlogLogin.as_view(), name='login'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('logout/', views.logout_page, name='logout'),
    path('api/blog-like/', views.api_total_like, name='api_like'),
    path('api/add-blog-like/', views.add_like, name='add_like'),
    path('api/category/', views.get_category, name='api_category'),
    path('api/add-blog-new/', views.add_blog_new, name='api_add_blog_new'),
    path('create-new-blog/', views.CreateNewBlog.as_view(), name='create_new_blog'),
]

# router = DefaultRouter()
# router.register(r'list', blog_list, basename='list')
# router.register(r'^category/<str:slug>', blog_pagination, basename='list')
# urlpatterns = outer.urlsr
