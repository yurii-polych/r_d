from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255, null=False)
    author = models.CharField(max_length=255, null=False)
    year = models.PositiveSmallIntegerField(null=False)
    price = models.FloatField(null=False)

    class Meta:
        db_table = 'book'
        unique_together = ('title', 'author')

    def __str__(self):
        return f'{self.id}. "{self.title}" {self.author}, {self.year}, price: {self.price}'
