from rest_framework import viewsets
from releasenotes.serializers import ReleaseNotesSerializer

from releasenotes.models import ReleaseNote


class ReleasenotesViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows releasenotes to be viewed or edited.
  """
  queryset = ReleaseNote.objects.all().order_by('app_version')
  serializer_class = ReleaseNotesSerializer
