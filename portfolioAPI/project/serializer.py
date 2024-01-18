from rest_framework import serializers
from project.models import Project
from certification.models import Language


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'title', 'description', 'tags', 'image', 'repository', 'url'
        ]
        read_only_fields = [
            'title', 'description', 'tags', 'image', 'repository', 'url'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        tags = []
        for tag in representation['tags']:
            tags.append(Language.objects.get(id=tag).name)
        representation['tags'] = tags
        return representation