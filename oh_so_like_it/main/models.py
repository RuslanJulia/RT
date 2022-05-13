from statistics import mode
from unicodedata import category, name
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'       

    class Meta:
        verbose_name_plural = "Категории"

class Sub_Category(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name_plural = "Подкатегории"


class Recepts(models.Model):
    name = models.CharField(max_length=50, null=False)
    photo = models.ImageField(blank=True, upload_to='images/')
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Sub_Category, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=10000)
    ingredients = models.CharField(max_length=10000)
    cooking_method = models.CharField(max_length=10000)
    date = models.DateField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепт'


class User(AbstractUser):
    email = models.EmailField(blank=True, unique=True, null=False)
    is_active = models.BooleanField(default=False)
    verification_code = models.IntegerField(default=0, null=False, blank=True)
    recept_id = models.ManyToManyField(Recepts, blank=True)
    count_comments = models.IntegerField(default=0)

class Comments(models.Model):
    recept_id = models.ForeignKey(Recepts, on_delete=models.CASCADE, null=True, blank=True, unique=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, unique=False)
    comment_date = models.DateField()
    comment = models.TextField()

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'