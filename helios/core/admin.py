from django.contrib import admin

from core import models


class TrackAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Track, TrackAdmin)
