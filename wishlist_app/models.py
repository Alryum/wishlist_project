from django.db import models
from django.urls import reverse
from users.models import CustomUser

class Wishlist(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='wishlists_images/', blank=True)
    description = models.TextField(max_length=200, blank=True)
    price = models.IntegerField(blank=True)
    link = models.URLField(blank=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='wishlists')

    def get_absolute_url(self):
        return reverse('detail_wishlist', kwargs={'pk': self.pk})
