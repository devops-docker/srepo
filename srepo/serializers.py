from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Build, Application


class BuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Build
        fields = ('id', 'application', 'created', 'branch', 'commitId', 'tag', 'location')


class ApplicationSerializer(serializers.ModelSerializer):
    builds = BuildSerializer(many=True,read_only=True)

    class Meta:
        model = Application
        fields = ( 'ID', 'name', 'builds')
