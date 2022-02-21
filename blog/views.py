
from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from rest_framework.response import Response
#
# from blog.models import Blog
# from blog.serializers import BlogSerializer
# from rest_framework.decorators import api_view
#
#
# @csrf_exempt
# @api_view(['GET', 'PUT', 'DELETE'])
# def blog_list(request):
#     try:
#         blog = Blog.objects.filter(is_public=True, is_removed=False)
#     except Blog.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = BlogSerializer(blog, many=True)
#         return Response({
#             'data': []
#         })
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = BlogSerializer(blog, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         blog.delete()
#         return HttpResponse(status=204)

from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from blog.models import Blog
from blog.serializers import BlogSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from datetime import date, datetime, timedelta
import arrow


class blog_list(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    # def logic(self):
    #     if up

    def list(self, request):
        queryset = Blog.objects.filter(
            is_public=True,
            is_removed=False,
            updated_at__range=[
                arrow.now().shift(days=-10).datetime, arrow.now().datetime
            ]
        )[:10]
        serializer = BlogSerializer(queryset, many=True)
        permission_class = AllowAny
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Blog.objects.all()
        blog = get_object_or_404(queryset, pk=pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

print([arrow.now().shift(days=-15), arrow.now()])
