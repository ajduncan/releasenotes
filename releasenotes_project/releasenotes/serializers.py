from rest_framework import serializers

from releasenotes.models import Releasenotes

class ReleaseNotesSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Releasenotes
    fields = ('hardware', 'model', 'firmware', 'app_version', 'app_platform',
              'mac_address', 'serial', 'language',)
