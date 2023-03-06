from django import forms
from .models import Wishlist
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CreateWishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['title', 'image', 'description', 'price', 'link']

        # widgets = {
        #     'title':forms.TextInput(attrs={'class': 'col-md-12 col-sm-12'}),
        #     'image':forms.ImageField(attrs={'class': 'col-md-12 col-sm-12'}),
        #     'description':forms.TextInput(attrs={'class': 'col-md-12 col-sm-12'}),
        # }
