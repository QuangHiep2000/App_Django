from django.contrib import admin
from blog.models import Blog, Category, BlogLike


# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('is_public', 'is_removed')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


@admin.register(BlogLike)
class CategoryAdmin(admin.ModelAdmin):
    pass

