from django.db import models
from django.utils import timezone
from houseplants.plants.models import Plant


class JournalTag(models.Model):
    tag = models.CharField(max_length=200)


class JournalEntry(models.Model):
    publish_date = models.DateTimeField(
        'publish date',
        default=timezone.now()
        )
    plant = models.ForeignKey(
        Plant,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    content = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(
        JournalTag,
        blank=True,
    )
