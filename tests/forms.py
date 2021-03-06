from django import forms
from django_prices.forms import AmountField

from . import models


class ModelForm(forms.ModelForm):
    class Meta:
        model = models.Model
        fields = ['price_net', 'price_gross']


class RequiredPriceForm(forms.Form):
    price_net = AmountField(currency='BTC')


class OptionalPriceForm(forms.Form):
    price_net = AmountField(currency='BTC', required=False)
