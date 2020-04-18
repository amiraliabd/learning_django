from rest_framework import serializers
from .models import Status

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image',
        ]
        read_only_fields = ['user']

    def validate_content(self, value):
        if len(value)>250:
            raise serializers.ValidationError('this is too long for content')
        return value

    def validate(self, data):
        content = data.get('content') or None
        image = data.get('image') or None
        if image is None and content is None:
            raise serializers.ValidationError('content or image is required')
        return data
