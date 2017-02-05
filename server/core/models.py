from django.db import models
from django.contrib.postgres.fields import JSONField

from django.conf import settings

from datetime import datetime, timedelta


class Track(models.Model):

    ip_address = models.GenericIPAddressField(protocol='IPv4', db_index=True)
    search_datetime = models.DateTimeField(auto_now_add=True)
    term = models.CharField(max_length=50, null=False, blank=False)
    result = JSONField(null=False, blank=True)

    class Meta:
        ordering = ['search_datetime']

    def as_report(self):
        return {
            'ip_address': self.ip_address,
            'search_datetime': self.search_datetime.strftime('%Y-%m-%d %H:%M %Z'),
            'term': self.term,
            'result': ', '.join('='.join((str(key), str(value))) for key, value in self.result.items())
        }


class GeographicCoordinate(models.Model):

    lat = models.FloatField(null=False, blank=False)
    lng = models.FloatField(null=False, blank=False)
    address = models.CharField(max_length=120, null=False, blank=False)

    class Meta:
        unique_together = ('lat', 'lng', 'address',)


class CacheResult(models.Model):
    lat = models.FloatField(null=False, blank=False)
    lng = models.FloatField(null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    cache_date = models.DateTimeField(auto_now=True)

    result = JSONField(null=False, blank=True)

    class Meta:
        unique_together = ('lat', 'lng',)
        index_together = [
            ('lat', 'lng'),
        ]


class CacheValidManager(models.Manager):

    def get_queryset(self):
        '''
            The caching mechanism is time-base
            You can set the expiration time in "settings.CACHE_VALIDATION_TIME_MINUTES"
        '''
        date_now = datetime.today()
        date_valid_cache = date_now - timedelta(minutes=settings.CACHE_VALIDATION_TIME_MINUTES)
        return super(CacheValidManager, self).get_queryset().filter(cache_date__range=(date_valid_cache, date_now))


class CacheValidResult(CacheResult):
    objects = CacheValidManager()

    class Meta:
        proxy = True
