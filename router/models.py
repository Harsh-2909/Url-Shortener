from django.db import models

# Create your models here.
class Route(models.Model):
    original_url = models.URLField()
    key = models.TextField()

    def __str__(self):
        return f"{self.key}"