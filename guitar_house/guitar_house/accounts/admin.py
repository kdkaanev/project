from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model


UserModel = get_user_model()
# Register your models here.
@admin.register(UserModel)
class GuitarHouseUserAdmin(admin.ModelAdmin):
    pass