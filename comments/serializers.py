from .models import Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    blog = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'comment', 'blog', 'user']

    def get_user(self, obj): # get user's username
        return obj.user.username if obj.user else None

    def get_blog(self, obj): # get blog title 
        return obj.blog.title if obj.blog else None