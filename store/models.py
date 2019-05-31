from django.db import models

from django.utils import timezone

class MainCategory(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Category(models.Model):
    main = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=15)
    material = models.CharField(max_length=30)
    content = models.TextField(default="")
    compatible = models.TextField(default="")
    status = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    def __str__(self):
        return self.name
        