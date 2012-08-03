from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField()


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
