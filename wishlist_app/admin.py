from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from .models import *

class WishlistAdmin(admin.ModelAdmin):
    # form = WishlistAdminForm
    list_display = ('title', 'description', 'image',
                    'price', 'link',)
    list_display_links = ('title',)
    fields = ('title', 'image', 'owner', 'description')

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')

    get_image.short_description = 'Фото'


admin.site.register(Wishlist, WishlistAdmin)