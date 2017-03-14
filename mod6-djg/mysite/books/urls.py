from django.conf.urls import url
from books.views import PublisherList, get_publisher, manage_books, manage_publishers2


app_name = 'books'

urlpatterns = [
    url(r'^publishers/$', PublisherList.as_view(), name='publishers'),
    url(r'^publisher/$', get_publisher, name='publisher_form'),
    # url(r'^manage-publishers/$', manage_publishers, name='manage_publisher_form'),
    url(r'^manage-publishers/$', manage_publishers2, name='manage_publisher_form'),
    url(r'^books/$', manage_books, name='books_form'),
    # ex: /books/5/
]