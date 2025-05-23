from django import forms
import datetime

class SpecForm(forms.Form):
    tscode = forms.CharField(label="Product Code")
    productname = forms.CharField()
    # date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), initial=datetime.date.today)
    color = forms.CharField()
    specific_gravity = forms.CharField()
    refractive_index = forms.CharField()
    flash_point = forms.CharField()
    shelf_life = forms.CharField(initial="12")
    supersede = forms.CharField(initial="0001")


class COAForm(forms.Form):
    tscode = forms.CharField(label="Product Code")
    productname = forms.CharField()
    batch = forms.CharField()
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    appearance = forms.CharField()
    odor = forms.CharField()
    specific_gravity = forms.CharField()
    refractive_index = forms.CharField()

class MSDSForm(forms.Form):
    tscode = forms.CharField(label="Product Code")
    productname = forms.CharField()
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    hazard = forms.CharField(widget=forms.Textarea)
    precaution = forms.CharField(widget=forms.Textarea)

from django import forms
from data_management.models import Main

class SelectCodeForm(forms.Form):
    code = forms.ChoiceField(label="Select Product Code")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        codes = Main.objects.values_list('code', flat=True).order_by('code')
        self.fields['code'].choices = [(c, c) for c in codes]
