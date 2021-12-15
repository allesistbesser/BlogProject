from django.contrib import admin

# Register your models here.
from .models import Category, Post , Comment, Like, PostView


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(PostView)