from rest_framework import serializers
from experience.models import Experience
from certification.models import Language

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = [
            'position', 'company', 'remote', 'location',
            'description', 'tech', 'start_date', 'end_date'
        ]
        read_only_fields = [
            'position', 'company', 'remote', 'location',
            'description', 'tech', 'start_date', 'end_date'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        tags = []
        for tag in representation['tech']:
            tags.append(Language.objects.get(id=tag).name)
        representation['tech'] = tags
        return representation