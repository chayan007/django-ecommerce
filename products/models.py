from django.db import models


class Products(models.Model):
    title = models.CharField()
    description = models.CharField()
    price = models.CharField()
    image = models.ImageField()

    def __str__(self):
        return self.title
