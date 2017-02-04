from django.db import models
from django.contrib.postgres.fields import JSONField


class Track(models.Model):

    ip_address = models.GenericIPAddressField(protocol='IPv4')
    search_datetime = models.DateTimeField(auto_now_add=True)
    term = models.CharField(max_length=50, null=False, blank=False)
    result = JSONField(null=False, blank=True)

    class Meta:
        ordering = ['search_datetime']

    def as_report(self):
        '''
        ass
        '''
        return {
            'ip_address': self.ip_address,
            'search_datetime': self.search_datetime.strftime('%Y-%m-%d %H:%M %Z'),
            'term': self.term,
            'result': ', '.join('='.join((str(key),str(value))) for key, value in self.result.items()) 
    }
