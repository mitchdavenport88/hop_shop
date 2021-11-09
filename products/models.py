from django.db import models
from PIL import Image


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=60)
    friendly_name = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Country(models.Model):

    class Meta:
        verbose_name_plural = 'Countries'

    name = models.CharField(max_length=60)
    friendly_name = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    name = models.CharField(max_length=60)
    sku = models.CharField(max_length=12, null=True, blank=True)
    description = models.TextField()
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    country = models.ForeignKey('Country', null=True, blank=True,
                                on_delete=models.SET_NULL)
    abv = models.DecimalField(max_digits=3, decimal_places=1)
    size = models.IntegerField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    # Code for image resizing was found here and edited accordingly
    # https://www.youtube.com/watch?v=CQ90L5jfldw
    def save(self):
        super().save()
        # Resizes image uploaded
        if self.image:
            uploaded_img = Image.open(self.image.path)
            if uploaded_img.height > 540 or uploaded_img.width > 540:
                output_size = (540, 540)
                uploaded_img.thumbnail(output_size)
                uploaded_img.save(self.image.path)
