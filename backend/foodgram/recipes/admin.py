from django.contrib import admin

from recipes.models import Tags


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass
