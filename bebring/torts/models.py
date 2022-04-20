from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import phone_regex_validator
from django.utils.safestring import mark_safe

# Create your models here.


class Tort(models.Model):
    """Моделька торта"""
    name = models.CharField(max_length=50, verbose_name='Название')
    cost = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    description = models.TextField(max_length=10000, verbose_name='Описание')
    category = models.ForeignKey('Category', models.PROTECT, null=True, blank=True, verbose_name='Категория')
    main_photo = models.ImageField(upload_to='photos/maintort_photos/', blank=True, verbose_name='Фото')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/tort/{self.pk}'

    class Meta:
        verbose_name = 'Торт'
        verbose_name_plural = 'Торты'
        ordering = ['name']


class TortPhoto(models.Model):
    tort_photo = models.ImageField(upload_to='photos/%Y/%m%d/', blank=True, verbose_name='Фото')
    product = models.ForeignKey(Tort, on_delete=models.CASCADE, related_name='photos')


class Category(models.Model):
    """Модель категории для тортов"""
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=10000)
    photo = models.ImageField(upload_to='photos/category_photos/', blank=True, verbose_name='Фото')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/category/{self.pk}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


# class User(DjUser):
#     """user model"""


class Offer(models.Model):
    """Offer for making tort"""

    name = models.CharField(max_length=50)
    phone_number = models.CharField(validators=[phone_regex_validator], max_length=17, null=True)
    description = models.TextField(max_length=10000)
    status = models.ForeignKey('StatusForOffer', models.CASCADE, verbose_name='Статус', default=1)
    # user = models.ForeignKey()
    tort = models.ForeignKey('Tort', models.CASCADE, verbose_name='Заказанный торт', default=1)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ' + self.pk


class StatusForOffer(models.Model):
    """Status for offer"""
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Статус: ' + self.name

    class Meta:
        verbose_name = 'Статус для заказов'
        verbose_name_plural = 'Статусы для заказов'


class StatusForProblem(models.Model):
    """Status for offer"""
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Статус: ' + self.name

    class Meta:
        verbose_name = 'Статус для проблем'
        verbose_name_plural = 'Статусы для проблем'



class Problem(models.Model):
    """Problem object to solve"""
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=10000)
    problem_photo = models.ImageField(upload_to='photos/problem_photos/%Y/%m%d/', verbose_name='Фото')
    status = models.ForeignKey('StatusForProblem', models.CASCADE, verbose_name='Статус', default=1)
    tort = models.ForeignKey('Tort', models.CASCADE, verbose_name='Заказанный торт', default=1)
    phone_number = models.CharField(validators=[phone_regex_validator], max_length=17, null=True)
    # user = models.ForeignKey()

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="200" height="150" />' % (self.problem_photo))

    def __str__(self):
        return 'Проблема ' + self.name

    class Meta:
        verbose_name = 'Проблема'
        verbose_name_plural = 'Проблемы'


