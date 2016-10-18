from django.db import models
from django.conf.global_settings import LANGUAGES


class ReleaseNote(models.Model):

    hardware = models.CharField(max_length=100, null=True, blank=True, default='')
    model = models.CharField(max_length=100, null=True, blank=True, default='')
    firmware = models.CharField(max_length=100, null=True, blank=True, default='')
    app_version = models.CharField(max_length=100, null=True, blank=True, default='')
    app_platform = models.CharField(max_length=100, null=True, blank=True, default='')
    mac_address = models.CharField(max_length=20, null=True, blank=True, default='')
    serial = models.CharField(max_length=100, null=True, blank=True, default='')
    language = models.CharField(max_length=7, choices=LANGUAGES, blank=True, default='')

    class Meta:
        ordering = ('app_version',)
