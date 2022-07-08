from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from .models import Post,Author,User
from .filters import PostFilter
from .forms import PostForm


class PostList(ListView):
    model = Post
    ordering = '-time_create'
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 1


class PostView(ListView):
    model = Post
    ordering = '-time_create'
    template_name = 'post_search.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ProductCreateView(CreateView):
    template_name = 'post_add.html'
    form_class = PostForm


class ProductDeleteView(DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'


class ProductUpdateView(UpdateView):
    template_name = 'post_add.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)
