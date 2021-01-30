from django.db import models
from django.conf import settings


class Url(models.Model):
    httpurl = models.URLField()
    short_id = models.SlugField(primary_key=True)
    count = models.IntegerField(default=-1)

    def __str__(self):
        return self.short_id

    @property
    def short_url(self):
        return settings.BASE_SITE_URL + self.short_id + '/'

    def save(self, *args, **kwagrs):
        self.count += 1
        super().save(*args, **kwagrs)
