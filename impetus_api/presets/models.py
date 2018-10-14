from django.db import models


class Preset(models.Model):
    """
    Preset Model.

    Defines the attributes of a preset
    """

    name = models.CharField(max_length=100)
    summary = models.CharField(max_length=300, blank=True, default='')

    def __str__(self):
        """Preset console representation."""
        return f"name='{self.name}' summary='{self.summary}' >"
