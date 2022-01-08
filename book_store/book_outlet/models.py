from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.title}({self.rating})"


