from django.contrib import admin

from core import models


class TrackAdmin(admin.ModelAdmin):
    pass


class CacheResultAdmin(admin.ModelAdmin):
    pass


class GeographicCoordinateAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Track, TrackAdmin)
admin.site.register(models.GeographicCoordinate, GeographicCoordinateAdmin)
admin.site.register(models.CacheResult, CacheResultAdmin)
