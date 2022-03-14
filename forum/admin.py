from django.contrib import admin
from .models import Category, Story, Reply, ReplyComment


# Register your models here.
@admin.register(Story)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'content', 'content_safe', 'title',
                    # , 'category', 'last_activity_at', 'created_at',
                    # 'updated_at', 'scheduled_at', 'published_at', 'STORY_STATUS_CHOICES',
                    # 'status', 'closed', 'featured_until', 'featured',
                    # 'edited_at', 'num_views', 'num_likes', 'num_replies',
                    #  'num_comments', 'num_participants', 'ip_address',
                    # 'user_agent',
                    )
    # search_fields = ('title',)
    # list_filter = ('is_public', 'is_removed')
    # list_editable = ('total_likes', 'is_removed')
    # save_on_top = True

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'desc_safe', 'order',
                    'color_code',
                    )


@admin.register(Reply)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'story', 'reply_order', 'content',
                    'content_safe', 'removed', 'created_at', 'updated_at',
                    'ip_address', 'user_agent', 'edited_at', 'edited_by',
                    )

@admin.register(ReplyComment)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'reply', 'content', 'mention_to',
                    'removed', 'ip_address', 'user_agent',
                    )
