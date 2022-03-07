from django.contrib import admin
from blog.models import Blog, Category, BlogLike


# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'total_likes', 'is_removed', 'updated_at')
    search_fields = ('title',)
    list_filter = ('is_public', 'is_removed')
    list_editable = ('total_likes', 'is_removed')
    save_on_top = True

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


@admin.register(BlogLike)
class CategoryAdmin(admin.ModelAdmin):
    pass

