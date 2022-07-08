from django.urls import path
# Импортируем созданное нами представление
from .views import PostList, PostView


urlpatterns = [
   path('', PostList.as_view()),
   path('search', PostView.as_view()),
]