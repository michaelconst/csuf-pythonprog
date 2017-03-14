from django.db import models
from django.urls import reverse
#Used to generate urls by reversing the URL patterns

# Create your models here.

class Publisher(models.Model):
    """
        Publisher Model
    """
    # attributes
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    website = models.URLField()
    country = models.CharField(max_length=20,default='US')

    # Meta
    class Meta:
        ordering = ["country","name"]

    # string representation
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the Publisher.
        """
        return reverse('publisher-detail', args=[str(self.id)])


class Author(models.Model):
    """
        Author Model
    """
    # attributes
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    # Meta
    class Meta:
        ordering = ("first_name",)

    # string representation
    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('author-detail', args=[str(self.id)])


class Book(models.Model):
    """
        Book Model
    """
    # attributes
    title = models.CharField(max_length=50)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    # Meta
    class Meta:
        ordering = ("title",)

    # string representation
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('book-detail', args=[str(self.id)])