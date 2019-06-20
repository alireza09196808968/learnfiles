from django.db import models
from django.utils import timezone

# Create your models here.


class post(models.Model):
    STATUS_CHOICE = (
        ("draft" , "DRAFT"),
        ("published" , "PUBLISHED"),
    )
    title = models.CharField(max_length=60)
    slug = models.SlugField()
    body = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=60, choices = STATUS_CHOICE ,default = "DRAFT")
    def __str__(self):
        return "post object (id = {} ,title = {})".format( self.id ,self.title)