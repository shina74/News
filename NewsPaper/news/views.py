from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from .models import Post, Author, User
from .filters import PostFilter
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin


class PostList(ListView):
    model = Post
    ordering = '-time_create'
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 10


class PostView(ListView):
    model = Post
    ordering = '-time_create'
    template_name = 'post_search.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ProductCreateView(CreateView,LoginRequiredMixin):
    template_name = 'post_add.html'
    form_class = PostForm


class ProductDeleteView(DeleteView, LoginRequiredMixin):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'


class ProductUpdateView(UpdateView, LoginRequiredMixin):
    template_name = 'post_add.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)
