from django.db import models
from django_countries.fields import CountryField


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    country = CountryField()
    website = models.URLField()

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return 'id={}, name={}, websites={}'.format(self.id, self.name, self.website)

    def published_books(self):
        return len(self.book_set.all())

    published_books.integer = True
    published_books.short_description = '# of published books'


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    headshot = models.ImageField(upload_to='author_headshots', null=True, blank=True)
    born_at = models.DateField()
    died_at = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return 'id={}, {}, {}'.format(self.id, self.last_name, self.first_name)


class BookFormat(models.Model):
    book_format = models.CharField(max_length=6)

    def __str__(self):
        return self.book_format


class BookCategory(models.Model):
    category = models.CharField(max_length=10)

    def __str__(self):
        return self.category


class Book(models.Model):
    title = models.CharField(max_length=80)
    abstract = models.CharField(max_length=120, null=True, blank=True)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pub_date = models.DateField()
    isbn = models.CharField(max_length=30)
    book_cover = models.ImageField(upload_to='book_covers', null=True, blank=True)
    format = models.ForeignKey(BookFormat, on_delete=models.DO_NOTHING)
    category = models.ManyToManyField(BookCategory)
    ranking = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ["title", "pub_date"]

    def __str__(self):
        return 'id={}, {}, by {}, published {}'\
            .format(self.id, self.title, ', '.join([a.first_name + ' ' + a.last_name for a in self.authors.all()]),
                    self.publisher.name)

    def publisher_name(self):
        return self.publisher.name

    def authors_names(self):
        return ', '.join([a.first_name + ' ' + a.last_name for a in self.authors.all()])

    publisher_name.short_description = 'Publisher'
    authors_names.short_description = 'Authors'