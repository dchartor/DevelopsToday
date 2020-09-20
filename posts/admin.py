from django.contrib import admin

from .models import Post, Comment


class CommentInLine(admin.TabularInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]
    list_display = [
        'author',
        'title',
        'upvotes',
        'link',
    ]


admin.site.register(Post, PostAdmin)
