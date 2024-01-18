from rest_framework import serializers
from certification.models import Certification, Badges, Language


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['name']
        read_only_fields = ['name']

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = [
            'title', 'description', 'certification_id', 'platform',
            'tags', 'url'
        ]
        read_only_fields = [
            'title', 'description', 'certification_id', 'platform',
            'tags', 'url'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        tags = []
        for tag in representation['tags']:
            tags.append(Language.objects.get(id=tag).name)
        representation['tags'] = tags
        return representation


class BadgesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badges
        fields = ['title', 'badge', 'tags', 'url']
        read_only_fields = ['title', 'badge', 'tags', 'url']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        tags = []
        for tag in representation['tags']:
            tags.append(Language.objects.get(id=tag).name)
        representation['tags'] = tags
        return representation