from django.contrib import admin
from core.models.team import Team 


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "company", "created_at")
    search_fields = ("name",)
    list_filter = ("company",)
    readonly_fields = ("slug",)

    fieldsets = (
        ("Basic Info", {"fields": ("name", "company")}),
        ("Auto Fields", {"fields": ("slug",), "classes": ("collapse",)}),
    )
