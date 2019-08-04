from django.db import models


class PlanModel(models.Model):  # noqa: D101

    name = models.CharField(max_length=72)
    summary = models.CharField(max_length=300, blank=True, default='')

    def __str__(self):  # noqa: D105
        return f"name='{self.name}' summary='{self.summary}'"
