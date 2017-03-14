from django.contrib import admin
from .models import Publisher, Author, Book, BookCategory, BookFormat


# class BooksInLine(admin.StackedInline):
class BooksInLine(admin.TabularInline):
    model = Book
    extra = 2
    fieldsets = [
        (None, {'fields': ['title', 'authors']}),
        ("Publishing Information", {'fields': ['publisher', 'pub_date', 'isbn']}),
        ("Book Information", {'fields': ['format', 'category']})
    ]
    list_filter = ['pub_date']


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'website', 'published_books', 'address', 'city', 'state', 'country']
    fieldsets = [
        (None, {'fields': ['name', 'website']}),
        ('Address', {'fields': ['address', 'city', 'state', 'country']})
    ]
    inlines = [BooksInLine]
    list_filter = ['name', 'city']


class BookAdmin(admin.ModelAdmin):
    model = Book
    fieldsets = [
        (None, {'fields': ['title', 'authors']}),
        ("Publishing Information", {'fields': ['publisher', 'pub_date', 'isbn']}),
        ("Book Information", {'fields': ['format', 'category']})
    ]
    list_display = ['title', 'authors_names', 'publisher_name', 'pub_date', 'isbn']
    list_filter = ['pub_date']


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author)
admin.site.register(BookCategory)
admin.site.register(BookFormat)
admin.site.register(Book, BookAdmin)