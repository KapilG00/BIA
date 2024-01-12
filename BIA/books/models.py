from django.db import models


class Book(models.Model):
    book_id = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publication_date = models.DateField()
    genre = models.CharField(max_length=20)
    rating = models.FloatField(default=0.0)
    num_pages = models.PositiveIntegerField()

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super(Book, self).save(*args, **kwargs)
