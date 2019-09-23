from django import forms
from django.forms import widgets
from OnlineMarket.models import PRODUCT_CATEGORY_CHOICES, PRODUCT_OTHER_CHOICE


class StoreForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Name of product:')
    description = forms.CharField(max_length=2000, widget=widgets.Textarea, label='Product description:', required=False)
    category = forms.ChoiceField(label='Category', choices=PRODUCT_CATEGORY_CHOICES,
                                 initial=PRODUCT_OTHER_CHOICE, required=False
                                 )
    amount = forms.IntegerField(min_value=0, label='Amount:')
    price = forms.DecimalField(max_digits=7, decimal_places=2, label='Price:')