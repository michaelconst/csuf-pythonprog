import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'booksProject.settings')

import django
import datetime

django.setup()

from books.models import Publisher, Author, Book

#python script for generating some sample data
#this script deletes all the data, before populating the new data

def populate():
    clear_data()
    pubApress = add_publisher('Apress', '123 Main, NY, NY-11011','http://www.apress.com', 'USA')
    pubMcGraw = add_publisher('McGraw-Hill', '345 Main, Sn Jose, CA-96767', 'http://www.mcgrawhill.com', 'USA')
    pubBritish1 = add_publisher('British1', '678 Main, London, London-96767', 'http://www.british1.com', 'UK')

    authorAdrian = add_author('Adrian', 'Holovety', 'adrianh@email.com')
    authorNigel = add_author('Nigel', 'George', 'ng@email.com')
    authorJames = add_author('James', 'Bennet', 'jamesb@email.com')

    #authorsList = []
    #authorsList.append(authorAdrian)

    add_book('DJango Definitive Guide',authorAdrian,pubApress,datetime.datetime(2015, 8, 4, 12, 30, 45))
    add_book('DJango CMS', authorNigel, pubApress, datetime.datetime(2016, 8, 4, 12, 30, 45))


    # Print out what we have added to the user.
    for b in Book.objects.all():
        print("Book details: Title : {0}-Author:{1}-Publisher:{2}".format(b.title, b.authors.get(), b.publisher))

def clear_data():
    Publisher.objects.all().delete()
    Author.objects.all().delete()
    Book.objects.all().delete()


def add_author(fname,lname,email):
    author = Author.objects.get_or_create(first_name=fname, last_name=lname,email=email)[0]
    return author

def add_publisher(name,address,website,country):
    publisher = Publisher.objects.get_or_create(name=name, address=address,website=website,country=country)[0]
    return publisher

def add_book(title,authors,publisher,pdate):
    book = Book()
    book.title = title
    book.publisher = publisher
    book.publication_date = pdate
    book.save()
    book.authors.add(authors)
    #book1 = Book.objects.get_or_create(title=title,authors=authors,publisher=publisher,publication_date=pdate)[0]
    #author = Author.objects.get_or_create(first_name=fname, last_name=lname,email=email)[0]
    return book

# Start execution here!
if __name__ == '__main__':
    print("Starting Books population script...")
    populate()