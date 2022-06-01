from django.db import models


class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)

    author = models.CharField(max_length=200)

    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')

    genre = models.CharField(max_length=200)

    language = models.CharField(max_length=200)
    
    class Meta:
        ordering = ['title']

    def __str__(self):
        """String for representing the Model object."""
        return self.title
