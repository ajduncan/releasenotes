from rest_framework import viewsets
from releasenotes.serializers import ReleasenotesSerializer

from releasenotes.models import Releasenotes


class ReleasenotesViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows releasenotes to be viewed or edited.
  """
  queryset = Releasenotes.objects.all().order_by('app_version')
  serializer_class = ReleasenotesSerializer
