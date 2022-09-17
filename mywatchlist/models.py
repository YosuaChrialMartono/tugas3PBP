import jsonfield
from django.db import models

# Create your models here.
class Watchlist(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.DateField()
    review = models.TextField()
    the_json = jsonfield.JSONField()
