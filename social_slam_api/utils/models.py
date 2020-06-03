from django.contrib.auth import get_user_model
from django.db import models


class AbstractTimestamp(models.Model):
    """
    Abstract Base Model that handles recording temporal data.
    """
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)


class AbstractTitle(models.Model):
    """
    Abstract Base Model that holds a title and a description
    """
    class Meta:
        abstract = True

    title = models.TextField(max_length=256, null=True)
    description = models.TextField(max_length=2048, null=True)


class AbstractLedger(AbstractTimestamp):
    """
    Abstract Base Model that records User information with respect to creating, modifying, and deleting an object.
    """
    class Meta:
        abstract = True

    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True,
                                   related_name='%(class)s_created')
    last_modified_by = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE,
                                         related_name='%(class)s_modifications')