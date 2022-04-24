from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Metadata)
admin.site.register(models.RawData)
admin.site.register(models.ScienceKeyword)
admin.site.register(models.Label)
admin.site.register(models.ProgressState)
