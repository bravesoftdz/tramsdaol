from django.db import models
from django.contrib.postgres.fields import JSONField


class Track(models.Model):

    ip_address = models.GenericIPAddressField(protocol='IPv4')
    search_datetime = models.DateTimeField(auto_now_add=True)
    term = models.CharField(max_length=50, null=False, blank=False)
    result = JSONField(null=False, blank=True)

    def as_dict(self) -> dict:
        return {
            'id': self.ip_address,
            'search_datetime': self.search_datetime,
            'term': self.term,
            'result': self.result,
    }

    class Meta:
        ordering = ['search_datetime']
