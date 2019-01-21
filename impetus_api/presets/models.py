from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import fields


class Preset(models.Model):
    """
    Preset Model.

    Defines the attributes of a preset
    """

    name = models.CharField(max_length=100)
    summary = models.CharField(max_length=300, blank=True, default='')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = fields.GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        """Preset console representation."""
        return f"name='{self.name}' summary='{self.summary}' >"


class Entry(models.Model):
    """
    Entry Model.

    Defines the attributes of a entry
    """

    LOOP = 0
    TIMER = 1
    ENTRY_TYPES = (
        (LOOP, 'Loop'),
        (TIMER, 'Timer'),
    )

    entry_type = models.IntegerField(choices=ENTRY_TYPES)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = fields.GenericForeignKey()

    def __str__(self):
        """Entry console representation."""
        return f"entry wehey!!"


class Timer(models.Model):
    """
    Timer Model.

    Defines the attributes of a timer entry.
    """

    description = models.CharField(max_length=100)
    time = models.PositiveIntegerField(default=1)
    is_work = models.BooleanField(default=True)
    pause = models.BooleanField(default=False)

    entries = fields.GenericRelation(Entry)


class Loop(models.Model):
    """
    Loop Model.

    Defines the attributes of a loop entry.
    """

    description = models.CharField(max_length=100)
    rounds = models.PositiveIntegerField(default=1)
    # entries = models.ForeignKey(Timer, on_delete=models.CASCADE)

    entries = fields.GenericRelation(Entry)


def create_timer(description='Default timer description', time=5000, is_work=True, pause=False):  # noqa: ignore=D103
    timer = Timer(description=description, time=time, is_work=is_work, pause=pause)
    return timer


def create_loop(description='Default loop description', rounds= 3):  # noqa: ignore=D103
    loop = Loop(description=description, rounds=rounds)
    return loop


# from presets.models import Timer, Loop, Entry, create_loop, create_timer
# t1 = create_timer()
# t1.save()
# t2 = create_timer()
# t2.save()
# t3 = create_timer()
# t3.save()
# l1 = create_loop()
# l1.save()
# preset = Preset(name='My preset', summary='My preset summary')
