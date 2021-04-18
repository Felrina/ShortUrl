from django.db import models
from .utils import code_generator, create_shortcut
from django.conf import settings
from shortner.validators import validate_url
from django.urls import reverse

# Create your models here.

SHORTURL_MAX = getattr(settings, "SHORTURL_MAX", 15)

class UrlModels(models.Model):
    url = models.CharField(max_length=1000, validators=[validate_url])
    short_url = models.CharField(max_length=SHORTURL_MAX, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if self.short_url is None or self.short_url == '':
            self.short_url = create_shortcut(self)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.url

    def get_short_url(self):
        return "http://127.0.0.1:8000/{short_url}".format(short_url=self.short_url)