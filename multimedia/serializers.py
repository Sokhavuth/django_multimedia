# mysite/multimedia/serializers.py.

from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'post_id', 
            'title', 
            'slug', 
            'content', 
            'featured_image', 
            'is_published',
            'is_featured',
            'created_at',
            'video',
            'category',
            'tag',
            'author',
        )