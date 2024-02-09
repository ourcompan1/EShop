from django.db import models


# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    month_price = models.IntegerField()
    img = models.ImageField(upload_to='photos')

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'
