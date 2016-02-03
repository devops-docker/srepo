from django.shortcuts import render

# Create your views here.
from srepo.models import Build, Application
from rest_framework import viewsets
from srepo.serializers import BuildSerializer, ApplicationSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'builds': reverse('build-list', request=request, format=format),
        'apps': reverse('application-list', request=request, format=format)
    })


class BuildViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Build.objects.all().order_by('-created')
    serializer_class = BuildSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class ApplicationTagSearch (APIView):
    def get (self, request, pk, tag, format=None):
        builds = Build.objects.filter(
            application = pk
            ).filter(
            tag__contains = tag
            )
        serializer = BuildSerializer(builds, many=True)
        return Response(serializer.data)
