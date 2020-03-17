from django.db import models


class Entry(models.Model):

    word = models.CharField(
        max_length=200,
        db_index=True)

    gender = models.CharField(
        choices=(('M', 'Masculine'), ('F', 'Feminine'), ('B', 'Both')),
        max_length=3)