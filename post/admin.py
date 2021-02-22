from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user']
    search_fields = ['content']
    class Meta:
        model = Post

admin.site.register(Post)