from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    rating = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self):
        a = 0
        for i in Post.objects.filter(author=self).values('rating'):
            a = a + (i['rating'] * 3)
        for i in self.post_set.all():
            for j in i.comment_set.all().values('rating'):
                a = a + j['rating']
        for i in self.user.comment_set.all().values('rating'):
            a = a + i['rating']

        self.rating = a
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)


class Post(models.Model):
    article = 'AR'
    news = 'NW'

    TYPE = [
        (article, 'Статья'),
        (news, 'Новость')
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    field = models.CharField(max_length=2, choices=TYPE, default=article)
    time_create = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    head = models.CharField(max_length=250,default='None2')
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[:124] + '...'

    def __str__(self):
        return f'{self.author.user.username}: {self.head}'

    def get_absolute_url(self):
        return f'/news/{self.id}'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()