from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()


class ProjectSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class ProjectLogSerializer(serializers.Serializer):
    object_kind = serializers.CharField()
    event_type = serializers.CharField()
    user = UserSerializer()
    project = ProjectSerializer()
