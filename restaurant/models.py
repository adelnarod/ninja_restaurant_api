from django.db import models
from pydantic.dataclasses import dataclass
# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=64)
    restaurant_type = models.CharField(max_length=64)
    rating = models.IntegerField(default=0)
    search_terms = models.CharField(max_length=500, default=f'{name},{restaurant_type}')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.search_terms = ','.join([self.name, self.restaurant_type])
        return super().save(*args, **kwargs)
