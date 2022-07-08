from django_filters import FilterSet
from .models import Post,Author,User


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = ('author', 'head', 'time_create')
