from rest_framework import serializers
from presets.models import Preset


class PresetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preset
        fields = ('id', 'name', 'summary')
