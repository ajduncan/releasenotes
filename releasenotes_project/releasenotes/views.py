from rest_framework import renderers, viewsets
from rest_framework.decorators import detail_route

from releasenotes.serializers import ReleaseNotesSerializer
from releasenotes.models import ReleaseNote


class ReleasenotesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows releasenotes to be viewed or edited.
    """
    queryset = ReleaseNote.objects.all().order_by('app_version')
    serializer_class = ReleaseNotesSerializer

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        releasenote = self.get_object()
        return Response(releasenote.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
