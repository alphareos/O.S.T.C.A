from django.db import models

# Create your models here.
class Clients(models.Model):
    Name = models.CharField(max_length=100)
    Logo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return (self).Name
