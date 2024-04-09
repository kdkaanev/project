from django.contrib import admin
from django.contrib.auth import get_user_model

UserModel = get_user_model()


# Register your models here.
@admin.register(UserModel)
class GuitarHouseUserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'first_name',
        'last_name',
    )

    list_filter = (
        'is_active',
        'date_joined',
    )
    search_fields = (
        'email',

    )
    ordering = ('-date_joined',)

    actions = ['make_active', 'make_inactive']

    def make_active(self, request, queryset):
        queryset.update(is_active=True)
        self.message_user(request, "Selected users have been activated.")

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(request, "Selected users have been deactivated.")

    def first_name(self, obj):
        return obj.profile.first_name

    def last_name(self, obj):
        return obj.profile.last_name
