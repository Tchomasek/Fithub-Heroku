from django.contrib import admin
from .models import Exercise, Tag

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['name']
    # search_fields = ['content', 'tags', 'name']
    class Meta:
        model = Exercise
        db_table = 'name'

class TagAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    # search_fields = ['name']
    class Meta:
        model = Tag


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Tag, TagAdmin)
