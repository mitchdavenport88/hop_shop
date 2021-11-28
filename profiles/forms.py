from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', 'wishlist',)

    def __init__(self, *args, **kwargs):
        """
        Function sets auto focus to the first field,
        removes auto-generated input labels, inserts placeholders
        to replace them and assigns classes to fields
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'def_street_address': 'Address',
            'def_town_or_city': 'Town or City',
            'def_county': 'County or State',
            'def_postcode': 'Postcode',
        }

        self.fields['def_street_address'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'def_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
            self.fields[field].label = False
