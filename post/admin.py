from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'content', 'id', 'user']
    # search_fields = ['content', 'chat']
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)