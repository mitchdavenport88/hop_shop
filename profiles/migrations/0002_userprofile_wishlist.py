# Generated by Django 3.2.8 on 2021-11-16 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20211018_1434'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='wishlist',
            field=models.ManyToManyField(blank=True, default=None, to='products.Product'),
        ),
    ]
