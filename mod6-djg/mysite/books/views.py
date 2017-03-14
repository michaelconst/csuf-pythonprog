from django.views.generic import ListView
from books.models import Publisher
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory

from .forms import PublishersFormSet
from .model_forms import PublisherForm
from .models import Book, BookFormat
from .model_forms import publisher_form, model_formset
from django_countries import countries


class PublisherList(ListView):
    model = Publisher
    object_list_name = Publisher.objects.all
    template_name = 'books/publisher_list.html'


# def get_publisher(request):
#     if request.method == 'POST':
#         form = PublisherForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             return HttpResponseRedirect('/done/')
#     else:
#         # a GET method
#         form = PublisherForm()
#
#     return render(request, 'books/publisher-bootstrap.html', {'form': form})

def get_publisher(request):
    if request.method == 'POST':
        form = publisher_form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect('/done/')
    else:
        # a GET method
        form = publisher_form

    # return render(request, 'books/publisher-bootstrap.html', {'form': form})
    return render(request, 'books/publisher.html', {'form': form})


# def manage_publishers(request):
#     initial = {'city': 'NY', 'state': 'NY', 'country': 'US'}
#     if request.method == 'POST':
#         formset = PublishersFormSet(request.POST, initial=[initial] * 3)
#         if formset.is_valid():
#             pass
#     else:
#         formset = PublishersFormSet(initial=[initial] * 3)
#     return render(request, 'books/manage_publishers.html', {'formset': formset})

def manage_publishers2(request):
    initial = {'city': 'NY', 'state': 'NY', 'country': 'US'}
    if request.method == 'POST':
        formset = model_formset(request.POST)
        if formset.is_valid():
            pass
    else:
        formset = model_formset
    return render(request, 'books/manage_publishers.html', {'formset': formset})


def manage_books(request):
    BookInlineFormSet = inlineformset_factory(BookFormat, Book, fields=('title', 'format'))
    if request.method == "POST":
        formset = BookInlineFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/done/')
    else:
        formset = BookInlineFormSet()
    return render(request, 'books/manage_books.html', {'formset': formset})

