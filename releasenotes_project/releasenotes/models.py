from django.db import models


class ReleaseNote(models.Model):

    hardware = models.CharField(max_length=100, null=True, blank=True, default='')
    model = models.CharField(max_length=100, null=True, blank=True, default='')
    firmware = models.CharField(max_length=100, null=True, blank=True, default='')
    app_version = models.CharField(max_length=100, null=False, blank=False, default='')
    app_platform = models.CharField(max_length=100, null=False, blank=False, default='')
    mac_address = models.CharField(max_length=20, null=True, blank=True, default='')
    serial = models.CharField(max_length=100, null=True, blank=True, default='')
    language = models.CharField(max_length=7, null=False, blank=False, default='')
    html_response = models.TextField(null=False, blank=False, default='')

    class Meta:
        ordering = ('app_version',)
