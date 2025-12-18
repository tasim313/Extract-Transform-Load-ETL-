from django.contrib import admin
from django.utils.html import format_html
from core.models.company import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "logo_preview", "created_at")
    search_fields = ("name",)
    readonly_fields = ("slug", "logo_preview")

    fieldsets = (
        ("Basic Info", {"fields": ("name", "description")}),
        ("Media", {"fields": ("logo", "logo_preview")}),
        ("System", {"fields": ("slug",), "classes": ("collapse",)}),
    )

    def logo_preview(self, obj):
        if not obj.logo:
            return "No Logo"
        return format_html("<img src='{}' width='60'/>", obj.logo.url)

    logo_preview.short_description = "Preview"
