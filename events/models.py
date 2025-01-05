from django.db import models

# Create your models here.


class myevent(models.Model):
    title = models.CharField(max_length=200)
    body1 = models.TextField(blank=True)
    body2 = models.TextField(blank=True)
    body3 = models.TextField(blank=True)
    body4= models.TextField(blank=True)
    slug = models.SlugField()
    banner = models.ImageField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    