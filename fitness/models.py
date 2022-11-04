from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

class FitnessProgramm(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='fitness_programm/')
    context = RichTextUploadingField()

    def __str__(self):
        return self.title


class Article(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='articles/')
    context = RichTextUploadingField()

    def __str__(self):
        return self.title


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite_title = models.CharField(max_length=255)
    favorite_slug = models.SlugField()

    def __str__(self):
        return '{} - {}'.format(self.user, self.favorite_title)


class SiteInfo(models.Model):
    tg_link = models.CharField(max_length=255)
    wh_link = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    about = models.TextField()

    def __str__(self):
        return '{} - {}'.format(self.email, self.tel)





