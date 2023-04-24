from django.db import models


class Purchase(models.Model):
    user = models.ForeignKey('user.User', related_name='purchases', on_delete=models.CASCADE, null=False)
    book = models.ForeignKey('book.Book', related_name='purchases', on_delete=models.CASCADE, null=False)
    date = models.DateField()

    class Meta:
        db_table = 'purchase'
        ordering = ['-date']
