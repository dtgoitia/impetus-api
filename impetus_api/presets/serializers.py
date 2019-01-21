from rest_framework import serializers
from presets.models import Preset


class PresetSerializer(serializers.ModelSerializer):  # noqa: ignore=D101
    class Meta:
        model = Preset
        fields = ('id', 'name', 'summary', 'preset')
