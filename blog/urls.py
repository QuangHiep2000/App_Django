from django.urls import path

# from blog import views
from blog.views import blog_list
from rest_framework.routers import DefaultRouter
#
# urlpatterns = [
#     path('list/', views.blog_list),
# ]

router = DefaultRouter()
router.register(r'list', blog_list, basename='list')
urlpatterns = router.urls
