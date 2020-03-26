from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    product_name = models.CharField('Название продукта', max_length=100)
    sku = models.CharField("SKU", max_length=50)
    price = models.PositiveSmallIntegerField('Цена', default=0)
    amount = models.PositiveSmallIntegerField("Количество", default=0)
    description = models.TextField("Описание",)
    producer = models.ForeignKey('Producer', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'

class Producer(models.Model):
    name = models.CharField("Производитель", max_length=50)
    production_country = models.CharField("Страна", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    author_name = models.CharField("Имя автора", max_length=50)
    comment_text = models.CharField(max_length=300)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
