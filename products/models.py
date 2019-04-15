from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    image = models.ImageField(upload_to='/uploads')

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title