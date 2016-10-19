from rest_framework import serializers

from releasenotes.models import ReleaseNote


class ReleaseNotesSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = ReleaseNote
    fields = ('hardware', 'model', 'firmware', 'app_version', 'app_platform',
              'mac_address', 'serial', 'language', 'html_response',)
