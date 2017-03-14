from django.conf.urls import url
from books.views import PublisherList, get_publisher, manage_books, manage_publishers2


app_name = 'restaurants'

urlpatterns = [
    # url(r'^publishers/$', PublisherList.as_view(), name='publishers'),
]