from django.db import models
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser


class Dress(models.Model):
    name = models.CharField(verbose_name='название платья', max_length=255)
    compound = models.CharField(verbose_name='состав', max_length=255)
    color = models.CharField(verbose_name='цвет', max_length=255)
    price = models.CharField(verbose_name='цена', max_length=255)
    product_article = models.CharField(verbose_name='артикул', max_length=255)
    image1 = models.ImageField(verbose_name='фотография', upload_to='product_images/')
    image2 = models.ImageField(verbose_name='фотография', upload_to='product_images/')
    image3 = models.ImageField(verbose_name='фотография', upload_to='product_images/')
    image4 = models.ImageField(verbose_name='фотография', upload_to='product_images/')

    def __str__(self):
        return self.name


class Collections(models.Model):
    name = models.CharField(verbose_name='название коллекции', max_length=255)
    collection_photo = models.ImageField(verbose_name='фотография')
    photo1 = models.ManyToManyField('Photo')
    slug = models.SlugField(verbose_name='URL', max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    image = models.ImageField(upload_to='photo1/')


class Jackets(models.Model):
    name = models.CharField(verbose_name='название пиджака', max_length=255)
    compound = models.CharField(verbose_name='состав', max_length=255)
    color = models.CharField(verbose_name='цвет', max_length=255)
    price = models.CharField(verbose_name='цена', max_length=255)
    product_article = models.CharField(verbose_name='артикул', max_length=255)
    image1 = models.ImageField(verbose_name='фотография', upload_to='product_images/')
    image2 = models.ImageField(verbose_name='фотография', upload_to='product_images/')
    image3 = models.ImageField(verbose_name='фотография', upload_to='product_images/')
    image4 = models.ImageField(verbose_name='фотография', upload_to='product_images/')

    def __str__(self):
        return self.name


class ShirtsAndBlouses(models.Model):
    name = models.CharField(verbose_name='название рубашки или блузы', max_length=255)
    compound = models.CharField(verbose_name='состав', max_length=255)
    color = models.CharField(verbose_name='цвет', max_length=255)
    price = models.CharField(verbose_name='цена', max_length=255)
    product_article = models.CharField(verbose_name='артикул', max_length=255)
    image1 = models.ImageField(verbose_name='фотография', upload_to='product_images/')
    image2 = models.ImageField(verbose_name='фотография', upload_to='product_images/')
    image3 = models.ImageField(verbose_name='фотография', upload_to='product_images/')
    image4 = models.ImageField(verbose_name='фотография', upload_to='product_images/')

    def __str__(self):
        return self.name


class TrousersAndSkirts(models.Model):
    name = models.CharField(verbose_name='название брюк или юбки', max_length=255)
    compound = models.CharField(verbose_name='состав', max_length=255)
    color = models.CharField(verbose_name='цвет', max_length=255)
    price = models.CharField(verbose_name='цена', max_length=255)
    product_article = models.CharField(verbose_name='артикул', max_length=255)
    image1 = models.ImageField(verbose_name='фотография', upload_to='product_images/')
    image2 = models.ImageField(verbose_name='фотография', upload_to='product_images/')
    image3 = models.ImageField(verbose_name='фотография', upload_to='product_images/')
    image4 = models.ImageField(verbose_name='фотография', upload_to='product_images/')

    def __str__(self):
        return self.name


class NewCollection(models.Model):
    name = models.CharField(verbose_name='название коллекции', max_length=255)
    compound = models.CharField(verbose_name='состав', max_length=255)
    color = models.CharField(verbose_name='цвет', max_length=255)
    price = models.CharField(verbose_name='цена', max_length=255)
    product_article = models.CharField(verbose_name='артикул', max_length=255)
    image1 = models.ImageField(verbose_name='фотография', upload_to='product_images/')
    image2 = models.ImageField(verbose_name='фотография', upload_to='product_images/')
    image3 = models.ImageField(verbose_name='фотография', upload_to='product_images/')
    image4 = models.ImageField(verbose_name='фотография', upload_to='product_images/')

    def __str__(self):
        return self.name
