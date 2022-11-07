from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import AbstractUser


# Пользовательский модель
class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


# Модель для фитнес-программ
class FitnessProgramm(models.Model):
    CHOICES = (
        ('Низкая интенсивность', 'Низкая интенсивность'),
        ('Умеренная интенсивность', 'Умеренная интенсивность'),
        ('Средняя интенсивность', 'Средняя интенсивность'),
        ('Большая интенсивность', 'Большая интенсивность'),
    )
    CHOICES_2 = (
        ('Для похудения', 'Для похудения'),
        ('Для набора мышечной массы', 'Для набора мышечной массы'),
    )
    CHOICES_3 = (
        ('Женщина', 'Женщина'),
        ('Мужчина', 'Мужчина'),
    )
    CHOICES_4 = (
        ('Руки', 'Руки'),
        ('Грудь', 'Грудь'),
        ('Спина', 'Спина'),
        ('Живот', 'Живот'),
        ('Ягодицы', 'Ягодицы'),
        ('Ноги', 'Ноги'),
    )



    slug = models.SlugField(verbose_name='Слоган')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    picture = models.ImageField(upload_to='fitness_programm/', verbose_name='Картинка')
    context = RichTextUploadingField(verbose_name='Контент')
    intensity = models.CharField(max_length=255, choices=CHOICES, blank=True, null=True, verbose_name='Вид Интенсивности')
    type = models.CharField(max_length=255, choices=CHOICES_2, blank=True, null=True, verbose_name='Тип программы')
    gender = models.CharField(max_length=255, choices=CHOICES_3, blank=True, null=True, verbose_name='Пол')
    part_of_body = models.CharField(max_length=255, choices=CHOICES_4, blank=True, null=True, verbose_name='Часть тела')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фитнес-программа"
        verbose_name_plural = "Фитнес-программы"


# Модель для Статьей
class Article(models.Model):
    slug = models.SlugField(verbose_name='Слоган')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    picture = models.ImageField(upload_to='articles/', verbose_name='Картинка')
    context = RichTextUploadingField(verbose_name='Контент')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


# Модель для Избранное
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Юзер')
    favorite_title = models.CharField(max_length=255, verbose_name='Заголовок')
    favorite_slug = models.SlugField(verbose_name='Слоган')

    def __str__(self):
        return '{} - {}'.format(self.user, self.favorite_title)

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные"


# Модель для информации о сайте
class SiteInfo(models.Model):
    tg_link = models.CharField(max_length=255, verbose_name='Телеграм ссылка')
    wh_link = models.CharField(max_length=255, verbose_name='Ватсапп ссылка')
    email = models.CharField(max_length=255, verbose_name='Почта')
    tel = models.CharField(max_length=255, verbose_name='Телефон номер')
    about = models.TextField(verbose_name='О нас')

    def __str__(self):
        return '{} - {}'.format(self.email, self.tel)


    class Meta:
        verbose_name = "Информация о сайте"
        verbose_name_plural = "Информации о сайте"



