from django import forms
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import LazyTypedChoiceField
from django_countries import countries


class PublisherForm(forms.Form):
    name = forms.CharField(label="Publisher's name", max_length=30)
    address = forms.CharField(label="Address", max_length=50)
    country = LazyTypedChoiceField(choices=countries)
    state = forms.CharField(max_length=20)
    city = forms.CharField(max_length=30)
    website = forms.URLField()


PublishersFormSet = forms.formset_factory(PublisherForm, max_num=3)