from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Accounts, Auction
from django.forms import ModelForm
from django.contrib.admin import widgets

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Accounts
        fields = ('username', 'email', 'dateofbirth')
        widgets = {
            'dateofbirth': forms.DateTimeInput(attrs={'class': 'datetime-dateofbirth'})
        }

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Accounts
        fields = ('username', 'email')

class AuctionForm(ModelForm):

    class Meta:
        model = Auction
        fields = ('Name', 'Description', 'Image', 'Stats', 'CurrentPrice')
        widgets = {
            'AuctionEnd': forms.DateTimeInput(attrs={'class': 'datetime-input'})
        }
