from django.db import models
from datetime import datetime


class Listing(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Главное фото')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото 1')
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото 2')
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото 3')
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото 4')
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото 5')
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото 6')
    is_published = models.BooleanField(default=True, verbose_name='Статус публикации')
    list_date = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
