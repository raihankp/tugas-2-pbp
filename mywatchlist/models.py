from logging.handlers import WatchedFileHandler
from django.db import models

# Create your models here.
class DataWatchlist(models.Model):
    watched = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    rating = models.IntegerField()
    release_date = models.CharField(max_length=255)
    review = models.CharField(max_length=255)