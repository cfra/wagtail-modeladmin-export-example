from django.db import models


class Person(models.Model):
    given_name = models.CharField(max_length=255)
    family_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.given_name} {self.family_name}"
