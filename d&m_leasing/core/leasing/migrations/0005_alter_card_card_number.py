# Generated by Django 5.0.2 on 2024-02-11 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leasing', '0004_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='card_number',
            field=models.CharField(max_length=20),
        ),
    ]
