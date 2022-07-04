from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    ordering = '-time_create'
    template_name = 'products.html'
    context_object_name = 'products'




class PostDetail(DetailView):
    model = Post
    template_name = 'product.html'
    context_object_name = 'product'
