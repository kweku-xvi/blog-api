from .models import Blog
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ['id', 'author', 'title', 'image', 'content', 'date_published', 'time_published']

        read_only_fields = ['id', 'author']

    def get_author(self, obj):
        return obj.author.username if obj.author else None