from django.core.management.base import BaseCommand
from models import Author, Book, BookFormat, BookCategory, Publisher


class Command(BaseCommand):
    help = 'Populate the database for the books app'

    def _create_book_formats(self):
        BookFormat.objects.create(book_format='hardcover')
        BookFormat.objects.create(book_format='softcover')

    def _create_book_categories(self):
        BookCategory.objects.create(category='fiction')
        BookCategory.objects.create(category='non-fiction')
        BookCategory.objects.create(category='travel')
        BookCategory.objects.create(category='scifi')
        BookCategory.objects.create(category='religious')
        BookCategory.objects.create(category='classics')
        BookCategory.objects.create(category='poetry')
        BookCategory.objects.create(category='foreign')

    def _create_publishers(self):
        Publisher.objects.create(name='',
                                 address='',
                                 city='',
                                 state='',
                                 country='US',
                                 website='')

    def handle(self, *args, **options):
        self._create_tags()