from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=100)

    def __str__(self):
        return "place %s" % self.name


class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "restaurant %s" % self.place.name


class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "waiter %s works at restaurant %s" % (self.name, self.restaurant)
