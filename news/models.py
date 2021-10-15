from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(null=True)
    content = models.TextField()

    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=200, default='ostca')

    def __str__(self):
        return (self).title

    def snippet(self):
        return self.content[:100] + '...'