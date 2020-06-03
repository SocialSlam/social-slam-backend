from django.db import models


class AbstractTimestamp(models.Model):

    class Meta:
        abstract = True

    created_at = models.DateTimeField()
    last_updated_at = models.DateTimeField()


class AbstractLedger(AbstractTimestamp):

    title = models.TextField(max_length=256, null=True)
    description = models.TextField(max_length=2048, null=True)