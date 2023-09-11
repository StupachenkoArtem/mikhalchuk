from django.db import models
from django.urls import reverse


class Clothes(models.Model):
    name = models.CharField(verbose_name='название платья', max_length=255)
    compound = models.CharField(verbose_name='состав', max_length=255)
    color = models.CharField(verbose_name='цвет', max_length=255)
    photo = models.ImageField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Collections(models.Model):
    name = models.CharField(verbose_name='название коллекции', max_length=255)
    photo = models.ImageField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
