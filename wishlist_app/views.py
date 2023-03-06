from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from users.models import CustomUser
from wishlist_app.forms import CreateWishlistForm
from wishlist_app.models import Wishlist
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy


def index(request):
    return render(request, 'wishlist_app/index.html')

def info(request):
    return render(request)


class UserWishlist(LoginRequiredMixin, ListView):
    model = Wishlist
    template_name = 'wishlist_app/user_wishlists.html'
    context_object_name = 'wishlists'
    paginate_by = 10
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_username = self.request.user.username
        context['wishlist_external_link'] = f"http://127.0.0.1:8000/view?u={current_username}"
        return context

    def get_queryset(self):
        return Wishlist.objects.filter(owner__username=self.request.user.username)


class ExternalView(ListView):
    model = Wishlist
    template_name = 'wishlist_app/external_view_list.html'
    context_object_name = 'wishlists'
    paginate_by = 10

    def get_queryset(self):
        return Wishlist.objects.filter(owner__username=self.request.GET.get('u'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['u'] = self.request.GET.get('u')
        return context


class DetailUserWishlist(DetailView):
    model = Wishlist
    template_name = 'wishlist_app/detail_wishlist.html'
    context_object_name = 'wishlist'
    allow_empty = True
    queryset = Wishlist.objects.select_related('owner')


class CreateWishlist(LoginRequiredMixin, CreateView):
    form_class = CreateWishlistForm
    template_name = 'wishlist_app/create_wishlist.html'
    login_url = '/login/'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class UpdateWishlist(LoginRequiredMixin, UpdateView):
    model = Wishlist
    template_name = 'wishlist_app/create_wishlist.html'
    fields = ['title', 'image', 'description', 'price', 'link']

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.owner != request.user:
            raise PermissionDenied()
        return super().post(request, *args, **kwargs)

    # def get_queryset(self):
    #     base_qs = super(UpdateWishlist, self).get_queryset()
    #     return base_qs.filter(owner=self.request.user)


class DeleteWishlist(LoginRequiredMixin, DeleteView):
    model = Wishlist
    template_name = 'wishlist_app/delete_wishlist.html'
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.owner != request.user:
            raise PermissionDenied()
        return super().post(request, *args, **kwargs)
