# mysite/multimedia/admin.py

from django.contrib import admin

from .models import Site, Category, Tag, Video, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class VideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    ordering = ['-created_at', '-id']

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    ordering = ['-created_at', '-id']


admin.site.register(Site)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Post, PostAdmin)