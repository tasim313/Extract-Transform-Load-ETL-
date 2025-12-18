from django.contrib import admin
from core.models.research_institution import ResearchInstitution

@admin.register(ResearchInstitution)
class ResearchInstitutionAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "website", "created_at")
    search_fields = ("name", "slug")
    list_filter = ("created_at",)
    ordering = ("name",)
    readonly_fields = ("created_at",)

    fieldsets = (
        ("Basic Information", {
            "fields": ("name", "slug", "description", "website")
        }),
        ("Branding", {
            "fields": ("logo",)
        }),
        ("System Fields", {
            "fields": ("created_at",),
        }),
    )
