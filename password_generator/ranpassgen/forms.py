from django import forms
from django.forms.widgets import NumberInput

class RangeInput(NumberInput):
    input_type = 'range'

class PassGenForm(forms.Form):
    length = forms.IntegerField(
        label='Password Length(4-64)',
        required=True,
        widget = RangeInput(attrs={'min':'1', 'max': '64', 'class': 'range', 'id': 'lengthRangeInput'})
    )

    include_symbols = forms.BooleanField(
        label='Include Symbols(@#$%^&!)',
        required=False,
        widget = forms.CheckboxInput(attrs={'class': 'checkboxInput'})
    )

    include_similar_characters = forms.BooleanField(
        label='Include Similar Characters(e.g 0o l1 2z)',
        required=False,
        widget = forms.CheckboxInput(attrs={'class': 'checkboxInput'})
    )

