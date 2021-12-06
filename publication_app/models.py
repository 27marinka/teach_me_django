from django.db import models

# Create your models here.


class Post(models.Model):
    create_date = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)
    title = models.CharField(max_length=256, unique=False, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    image = models.ImageField(null=True, blank=True)
