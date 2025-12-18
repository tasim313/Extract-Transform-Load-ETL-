from django.contrib import admin
from django import forms
from django.utils.html import format_html
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('slug', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


@admin.register(User)
class ETLUserAdmin(admin.ModelAdmin):
    form = UserAdminForm

    list_display = (
        "id", "email", "role", "status",
        "first_name", "last_name",
        "company_name", "is_active", "created_at_display",
    )

    list_filter = (
        "role", "status", "company", "university",
        "research_institution", "health_institution",
        "is_active", "is_staff",
    )

    search_fields = ("email", "first_name", "last_name", "phone")

    readonly_fields = (
        "slug", "is_superuser", "last_login",
    )

    fieldsets = (
        ("User Info", {
            "fields": (
                "email", "password",
                "first_name", "last_name", "phone",
                "profile_image", "role", "status",
            ),
        }),
        ("Organization", {
            "classes": ("collapse",),
            "fields": (
                "company", "team",
                "university", "research_institution",
                "health_institution",
            ),
        }),
        ("Permissions", {
            "classes": ("collapse",),
            "fields": ("is_active", "is_staff", "is_superuser",
                       "groups", "user_permissions"),
        }),
        ("System Info", {
            "classes": ("collapse",),
            "fields": ("slug", "last_login"),
        }),
    )

    def company_name(self, obj):
        return obj.company.name if obj.company else "—"
    company_name.short_description = "Company"

    def created_at_display(self, obj):
        return format_html(
            "<b style='color:#0284c7;'>{}</b>",
            obj.date_joined.strftime("%d %b %Y") if hasattr(obj, "date_joined") else "—"
        )
    created_at_display.short_description = "Created"


