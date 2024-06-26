from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.title
