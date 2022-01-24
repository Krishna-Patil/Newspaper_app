from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .forms import *
# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm


admin.site.register(CustomUser, CustomUserAdmin)
