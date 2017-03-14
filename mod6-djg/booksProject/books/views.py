from django.shortcuts import render
from django.views import generic

from books.models import Publisher, Author, Book


# Create your views here.
def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_authors = Author.objects.count()  # The 'all()' is implied by default.
    num_publishers = Publisher.objects.all().count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_authors': num_authors, 'num_publishers': num_publishers, 'num_visits':num_visits, },
    )


class BookListView(generic.ListView):
    model = Book



class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author


class PublisherListView(generic.ListView):
    model = Publisher


class PublisherDetailView(generic.DetailView):
    model = Publisher

