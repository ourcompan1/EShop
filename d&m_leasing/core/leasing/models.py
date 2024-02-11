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


class Feedback(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    text = models.TextField()

    def create_question(self, name, email, text):
        self.name = name
        self.email = email
        self.text = text
        self.save()

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedback'


class Card(models.Model):
    car_name = models.CharField(max_length=200)
    card_number = models.CharField(max_length=20)
    owner_name = models.CharField(max_length=200)
    date = models.CharField(max_length=5)
    cvv = models.IntegerField()

    def create_card(self, car_name, card, owner_name, date, cvv):
        self.car_name = car_name
        self.card_number = card
        self.owner_name = owner_name
        self.date = date
        self.cvv = cvv
        self.save()

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'
