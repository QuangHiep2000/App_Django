from django.core.paginator import Paginator
from django.views.generic import TemplateView

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from blog.models import Blog, Category
from blog.serializers import BlogSerializer
from rest_framework.decorators import api_view


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def blog_list(request):
    try:
        blog = Blog.objects.filter(is_public=True, is_removed=False)
    except Blog.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BlogSerializer(blog, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BlogSerializer(blog, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        blog.delete()
        return HttpResponse(status=204)


# @csrf_exempt
# @api_view(['GET', 'PUT', 'DELETE'])
class CategoryPagination(TemplateView):
    template_name = "blog/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            # blog = Blog.objects.filter(is_public=True, is_removed=False)
            category = Category.objects.get(slug=kwargs.get('slug'))
        except Blog.DoesNotExist:
            return HttpResponse(status=404)
        queryset = Blog.objects.filter(
            is_public=True,
            is_removed=False,
            category=category.id
        )
        permission_class = AllowAny
        page_number = self.request.GET.get('page', '')
        paginator = Paginator(queryset, 2)
        page_obj = paginator.get_page(page_number)
        if self.request.method == 'GET':
            serializer = BlogSerializer(page_obj, many=True)
            context['data_list'] = serializer.data
            return context


class AdminPage(TemplateView):
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Blog.objects.filter(
            is_public=True,
            is_removed=False,
        ).order_by('-created_at')[:5]
        permission_class = AllowAny
        if self.request.method == 'GET':
            serializer = BlogSerializer(queryset, many=True)
            context['data_list_new'] = serializer.data
            print(serializer.data)
            return context

