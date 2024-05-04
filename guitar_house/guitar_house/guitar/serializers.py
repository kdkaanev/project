from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='user.profile.full_name')

    class Meta:
        model = Review

        fields = ['text', 'rating', 'created_at', 'guitar', 'name']
