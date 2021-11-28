from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
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

    def generate_sku(self):
        """ Function creates a sku for a newly added product """
        if self.category:
            sku_category = self.category.friendly_name[:2].upper()
        else:
            sku_category = '--'

        if self.country:
            sku_country = self.country.friendly_name[:2].upper()
        else:
            sku_country = '--'

        sku_pk = self.pk

        sku = f'THS/{sku_category}/{sku_pk}{sku_country}'
        return sku

    # Code for image resizing was found here and edited accordingly
    # https://www.youtube.com/watch?v=CQ90L5jfldw
    def save(self, *args, **kwargs):
        """ Function resizes the image uploaded if required """
        super().save(*args, **kwargs)
        if self.image:
            uploaded_img = Image.open(self.image)
            if uploaded_img.height > 540 or uploaded_img.width > 540:
                output_size = (540, 540)
                uploaded_img.thumbnail(output_size)
                uploaded_img.save(self.image.name)


@receiver(post_save, sender=Product)
def add_sku(sender, instance, created, **kwargs):
    """ Calls the generate_sku function in the above class """
    if created:
        instance.sku = instance.generate_sku()
        instance.save()
