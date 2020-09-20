from rest_framework import serializers

from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "title", "link", "upvotes", "author", "created_at")
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "author", "content", "created_at", "post")
        model = Comment
