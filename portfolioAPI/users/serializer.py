from rest_framework import serializers
from users.models import User, AdminData, AreaOfInterest, AdminDomain

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminData
        fields = [
            'email', 'phone',
            'instagram', 'twitter', 'linkedin', 'github',
            'city', 'state', 'country',
            'about', 'tagline',
            'domains', 'interests',
            'picture'
        ]
        read_only_fields = fields

    def to_representation(self, instance):
        representaion = super().to_representation(instance)
        user = User.objects.all()
        domain = AdminDomain.objects.all()
        interest = AreaOfInterest.objects.all()
        if user.exists():
            representaion['username'] = user[0].username
            representaion['name'] = user[0].name
        else:
            representaion['username'] = None
            representaion['name'] = None

        if domain.exists():
            representaion['domains'] = [d.domain for d in domain]
        else:
            representaion['domains'] = None

        if interest.exists():
            representaion['interests'] = [i.area for i in interest]
        else:
            representaion['interests'] = None
        return representaion
