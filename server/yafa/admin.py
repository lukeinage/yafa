from django.contrib import admin

from . import models

admin.site.register(models.Site)
admin.site.register(models.Zone)
admin.site.register(models.Advert)

