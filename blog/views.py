from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django import forms
from django.db.models.signals import post_save
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from blog.models import Blog, Category, BlogLike
from blog.forms import LoginForm
from blog.serializers import BlogSerializer, BlogLikeSerializer, CategorySerializer
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
class CategoryPagination(LoginRequiredMixin, TemplateView):
    template_name = "blog/category.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        try:
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
            context['page_number'] = page_number
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
            return context


# class BlogSlug(LoginRequiredMixin, TemplateView):
class BlogSlug(TemplateView):
    template_name = "blog/blog_slug.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            # category = Category.objects.get(slug=kwargs.get('slug'))
            blog = Blog.objects.get(slug=kwargs.get('slug'))
        except Blog.DoesNotExist:
            return HttpResponse(status=404)
        queryset = Blog.objects.filter(
            is_public=True,
            is_removed=False,
            category=blog.category
        )
        permission_class = AllowAny

        if self.request.method == 'GET':
            user = self.request.user
            serializer = BlogSerializer(queryset, many=True)
            context['data_list_blog_slug'] = serializer.data
            context['blog_detail'] = blog
            # context['slug'] = kwargs.get('slug')
            # print(is_my_blog)
            # context['is_my_blog'] = is_my_blog
            return context


# class BlogLogin(TemplateView):
#     template_name = "blog/login.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         form = LoginForm()
#         context['form_data'] = form
#         return context


class BlogLogin(LoginView):
    template_name = "blog/login.html"


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email')
        field_classes = {'username': UsernameField}


class RegisterPage(FormView):
    template_name = "blog/register.html"
    form_class = RegisterForm

    def form_valid(self, form):
        data = form.cleaned_data
        User.objects.create_user(
            username=data['username'],
            password=data['password1'],
            email=data['email']
        )
        return redirect('/login/')


class ProfilePage(LoginRequiredMixin, TemplateView):
    template_name = "blog/profile.html"


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def api_total_like(request):
    user = request.user
    slug = request.GET.get('slug')

    if not slug:
        return Response({
            'ok': False
        })

    if not user.is_authenticated:
        return Response({
            'ok': False
        })
    blog = Blog.objects.filter(
        is_public=True,
        is_removed=False,
        slug=slug
    ).only('total_likes').first()
    if not blog:
        return Response({
            'ok': False
        })

    user = User.objects.get(
        username=user.username
    )

    if BlogLike.objects.filter(
            user=user,
            blog=blog
    ).exists():
        check_like = True
    else:
        check_like = False
    return Response({
        'ok': True,
        'data': {
            'isLiked': check_like,
            'totalLikes': blog.total_likes,
            'user': str(user)
        }
    })


@csrf_exempt
@api_view(['POST'])
def add_like(request):
    if request.method == 'POST':
        user = request.user
        if not user.is_authenticated:
            return Response({
                'ok': False,
                'msg': "Ban chua dang nhap"
            })
        slug = request.data.get('slug')
        try:
            blog = Blog.objects.get(slug=slug)
        except Blog.DoesNotExist:
            return Response({
                'ok': False
            })
        BlogLike.objects.create(user=user, blog=blog)
        return Response({
            'ok': True
        })


@csrf_exempt
@api_view(['GET'])
def get_category(request):
    user = request.user
    if not user.is_authenticated:
        return Response({
            'ok': False,
            'msg': "Ban chua dang nhap"
        })
    category = Category.objects.all()
    if not category:
        return Response({
            'ok': False
        })
    serializer = CategorySerializer(category, many=True)
    return Response({
        'ok': True,
        'data': serializer.data
    })


@csrf_exempt
@api_view(['POST'])
def add_blog_new(request):
    user = request.user
    data = request.data
    title = data.get('title', '')
    content = data.get('content', '')
    if not user.is_authenticated:
        return Response({
            'ok': False,
            'msg': "Ban chua dang nhap"
        })
    try:
        category = Category.objects.get(name=request.data.get('category', ''))
    except Category.DoesNotExist:
        return Response({
            'ok': False
        })

    # blog_data = JSONParser().parse(request)
    blog_slug = Blog.objects.create(
        category=category,
        title=title,
        content=content,
        is_public=True,
        user=user,
    )
    return Response({
        'ok': True,
        'slug': blog_slug.slug
    })


class CreateNewBlog(TemplateView):
    template_name = 'blog/create_new_blog.html'


@csrf_exempt
@api_view(['GET'])
def api_my_blog(request):
    user = request.user
    slug = request.GET.get('slug')

    if not slug:
        return Response({
            'ok': False
        })

    if not user.is_authenticated:
        return Response({
            'ok': False
        })

    user = User.objects.get(
        username=user.username
    )
    blog = Blog.objects.filter(
        is_public=True,
        is_removed=False,
        slug=slug,
        user=user
    ).first()
    print(blog)
    if blog:
        print(True)
        current_category = Category.objects.get(id=blog.category.id)
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response({
            'ok': True,
            'data': {
                'title': blog.title,
                'content': blog.content,
                'currentCategory': current_category.name,
                'category': serializer.data,
            },
            'isMyBlog': True
        })
    else:
        print(False)
        return Response({
            'ok': False,
            'isMyBlog': False
        })


@csrf_exempt
@api_view(['PUT'])
def edit_blog(request):
    user = request.user
    data = request.data
    title = data.get('title', '')
    content = data.get('content', '')
    slug = data.get('slug', '')
    if not user.is_authenticated:
        return Response({
            'ok': False,
            'msg': "Ban chua dang nhap"
        })
    try:
        category = Category.objects.get(name=request.data.get('category', ''))
    except Category.DoesNotExist:
        return Response({
            'ok': False
        })
    Blog.objects.filter(slug=slug).update(
        category=category,
        title=title,
        content=content
    )

    return Response({
        'ok': True,
        # 'slug': blog_update.slug,
    })


class EditBlog(TemplateView):
    template_name = 'blog/edit_blog.html'


def logout_page(request):
    logout(request)
    return redirect('/login/')


@csrf_exempt
@api_view(['GET'])
def get_content_blog(request, **kwargs):
    slug = request.GET.get('slug', '')
    blog = Blog.objects.get(
        is_public=True,
        is_removed=False,
        slug=slug
    )

    return Response(
        {
            'ok': True,
            'data': {
                'user': blog.user.username,
                'title': blog.title,
                'content_safe': blog.content_safe,
                'create_at': blog.created_at
            }
        }
    )


class BlogListAPIView(ListAPIView):
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Blog.objects.filter(
            is_public=True,
            is_removed=False).order_by('created_at')

        # serializer_class = BlogSerializer(qs, many=True)
        # print(serializer_class.data)
        return queryset


class BlogListCategoryAPIView(ListAPIView):
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        slug = self.request.GET.get('slug', '')
        if not slug:
            return []

        _blog = Blog.objects.filter(
            slug=slug
        ).only('id', 'category_id').first()
        if not _blog:
            return []
        blog = Blog.objects.select_related('category').filter(
            is_public=True,
            is_removed=False,
            category_id=_blog.category_id
        ).exclude(id=_blog.id).order_by('-created_at')[:3]

        return blog


@csrf_exempt
@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        user = request.data.get('username', '')
        password = request.data.get('password', '')
        print(user)
        _user = User.objects.get(username=user)
        if not _user:
            return Response({
                'ok': False
            })
        print(_user.password)
        if _user.password == password:
            print("da dang nhap")
            return Response({
                'ok': True
            })