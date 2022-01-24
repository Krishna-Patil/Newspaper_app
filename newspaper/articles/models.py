from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )
    date = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('article_list')

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='comments')
    comment = models.CharField(max_length=150)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('article_list')
