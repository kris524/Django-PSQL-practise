from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Address(models.Model):
    street = models.CharField(max_length=200)
    number = models.PositiveIntegerField()
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.street
