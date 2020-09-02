from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Accounts ,Auction

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Accounts
    list_display = ['email', 'username',]

admin.site.register(Accounts, CustomUserAdmin)
admin.site.register(Auction)