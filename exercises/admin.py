from django.contrib import admin
from .models import Exercise, Tag

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user']
    search_fields = ['content', 'tags']
    class Meta:
        model = Exercise

class TagAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user']
    search_fields = ['name']
    class Meta:
        model = Tag


admin.site.register(Exercise)
admin.site.register(Tag)
