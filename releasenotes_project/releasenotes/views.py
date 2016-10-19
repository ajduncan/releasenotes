from rest_framework import renderers, viewsets
from rest_framework.decorators import detail_route
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from releasenotes.serializers import ReleaseNotesSerializer
from releasenotes.models import ReleaseNote


class ReleasenotesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows releasenotes to be viewed or edited.
    """
    queryset = ReleaseNote.objects.all().order_by('app_version')
    serializer_class = ReleaseNotesSerializer
    permission_classes = (AllowAny,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        releasenote = self.get_object()
        return Response(releasenote.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        try:
            app_details = ReleaseNote.objects.get(
                app_version=request.POST.get('app_version'),
                app_platform=request.POST.get('app_platform'),
                language=request.POST.get('language'))

            return Response({'html': app_details.html_response})
        except ReleaseNote.DoesNotExist:
            return Response({'html': ''})

    def update(self, request, *args, **kwargs):
        return Response({'html': ''})

    def destroy(self, request, *args, **kwargs):
        return Response({'html': ''})
