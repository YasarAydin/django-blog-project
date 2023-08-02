from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "is_active", "slug", "selected_categories"]
    list_editable = ["is_active"]
    search_fields = ["title", "description"]
    readonly_fields = ["slug"]
    list_filter = ["is_active", "categories"]

    def selected_categories(self, obj):
        html = "<ul>"
        for category in obj.categories.all():
            html += "<li>" + category.name + "</li>"
        html += "</ul>"
        return mark_safe(html)

admin.site.register(models.BlogModel, BlogAdmin)

admin.site.register(models.Category)
