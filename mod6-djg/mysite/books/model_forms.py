from django.forms import ModelForm, Select, modelformset_factory
from .models import Publisher, Author, Book, BookFormat, BookCategory
from django.forms import modelform_factory
from django_countries import countries


class BookFormatForm(ModelForm):
    class Meta:
        model = BookFormat
        fields = ['book_format']


class Book(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'pub_date', 'format']


class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'address', 'city', 'state', 'country', 'website']


publisher_form = modelform_factory(Publisher, fields=['name', 'address', 'city', 'state', 'country', 'website'],
                                   widgets={'country': Select(choices=countries)})


ModelPublisherFormset = modelformset_factory(Publisher, fields=('name', 'website'), max_num=3, extra=2)
model_formset = ModelPublisherFormset(queryset=Publisher.objects.filter(name__startswith='S'))