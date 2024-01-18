from rest_framework import serializers
from education.models import Education, Achievement

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = [
            'institute', 'location', 'degree', 'specialization',
            'start_date', 'end_date', 'grade_style', 'grade'
        ]
        read_only_fields = [
            'institute', 'location', 'degree', 'specialization',
            'start_date', 'end_date', 'grade_style', 'grade'
        ]

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ['title', 'description']
        read_only_fields = ['title', 'description']