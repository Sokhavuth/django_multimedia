# mysite/multimedia/models.py
 
from djongo import models
 
from uuid import uuid4
 
# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.CharField(max_length=255)
 
    def __str__(self):
        return self.name
 
 
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    description = models.TextField(blank=True)
 
    class Meta:
        verbose_name_plural = "categories"
 
    def __str__(self):
        return self.name 
 
 
class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    description = models.TextField(blank=True)
 
    def __str__(self):
        return self.name 
 
 
class Video(models.Model):
    TYPE_OF_VIDEO = [
        ('YouTube', 'YouTube'),
        ('YouTubePL', 'YouTubePL'),
        ('Facebook', 'Facebook'),
        ('OK', 'OK'),
        ('Vimeo', 'Vimeo')
    ]
 
    STATUS_OF_VIDEO = [
        ('ចប់​ហើយ', 'ចប់​ហើយ'),
        ('នៅ​មាន​​ត', 'នៅ​មាន​​ត')
    ]
    
    title = models.CharField(max_length=255, blank=True)
    slug = models.SlugField()
    type = models.CharField(max_length=255, choices=TYPE_OF_VIDEO, default='YouTube')
    video_id = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=STATUS_OF_VIDEO, default='នៅ​មាន​​ត')
    created_at = models.DateField(auto_now=True)
 
    class Meta:
        ordering = ['created_at','id']
 
    def __str__(self):
        return self.slug
 

from ckeditor.fields import RichTextField
from django.conf import settings
 
class Post(models.Model):
    PUBLISHED = [
        ('yes', 'ត្រូវ​បាន​ចុះ​ផ្សាយ'),
        ('no', 'មិន​ទាន់​ចុះ​ផ្សាយ')
    ]

    id = models.CharField(primary_key=True, max_length=255,default=uuid4().hex, editable=False) 
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    content = RichTextField(blank=True)
    featured_image = models.CharField(max_length=255)
    is_published = models.CharField(max_length=255, choices=PUBLISHED, default='yes')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True)
    video = models.ManyToManyField(Video, blank=True)
    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
 
    class Meta:
        ordering = ['-created_at']
 
    def __str__(self):
        return self.title 