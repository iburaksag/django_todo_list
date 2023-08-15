from django.contrib import admin
from .models import Todo, Category, Tag


class TodoAdmin(admin.ModelAdmin):
    list_display= [
        'pk',
        'category',
        'title',
        'is_active',
        # 'created_at',
        # 'updated_at',
    ]
    list_display_links = [
        'pk',
        'category',
        'title'
    ]

class CategoryAdmin(admin.ModelAdmin):
    list_display= [
        'pk',
        'title',
        'is_active',
    ]


admin.site.register(Todo, TodoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
