from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Country


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('sku',)

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'description': 'Description',
            'category': 'Category',
            'country': 'Country',
            'abv': 'ABV %',
            'size': 'Size (ml)',
            'price': 'Price (£)',
            'image': 'Image',
        }
        categories = Category.objects.all()
        category_friendly_names = [(None, 'None Selected')] + [
            (c.id, c.get_friendly_name()) for c in categories]
        countries = Country.objects.all()
        country_friendly_names = [(None, 'None Selected')] + [
            (country.id, country.get_friendly_name()) for country in countries]

        self.fields['category'].choices = category_friendly_names
        self.fields['country'].choices = country_friendly_names
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country' or field != 'category':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'product-form-input'
