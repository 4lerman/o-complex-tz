from django.db import models


class WeatherQuery(models.Model):
    city = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.city
