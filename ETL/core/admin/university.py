from django.contrib import admin
from django.utils.html import format_html
from core.models.university import University

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "logo_preview", "website", "created_at")
    search_fields = ("name",)
    readonly_fields = ("slug", "logo_preview")

    def logo_preview(self, obj):
        return format_html("<img src='{}' width='60'/>", obj.logo.url) if obj.logo else "N/A"
