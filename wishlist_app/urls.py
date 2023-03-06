from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('info/', info, name='info'),
    path('wishlist/<str:username>', UserWishlist.as_view(), name='user_wishlist'),
    path('view/', ExternalView.as_view(), name='external_reference'),
    path('createlist/', CreateWishlist.as_view(), name='create_wishlist'),
    path('list/<int:pk>', DetailUserWishlist.as_view(), name='detail_wishlist'),
    path('update/<int:pk>', UpdateWishlist.as_view(), name='update_wishlist'),
    path('delete/<int:pk>', DeleteWishlist.as_view(), name='delete_wishlist'),
]