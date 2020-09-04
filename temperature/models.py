from django.db import models
from bulk_update_or_create import BulkUpdateOrCreateQuerySet


class Temperature(models.Model):
    """
    Temperature basic model.
    """

    uuid = models.IntegerField(unique=True)
    timestamp = models.DateTimeField(
        null=True,
        blank=True,
    )
    temperature = models.FloatField(
        null=True, 
        blank=True, 
        default=None,
    )
    duration = models.CharField(
        blank=True,
        null=True,
        max_length=250,
    )

    objects = models.Manager() # The default manager.
    bulk_objects = BulkUpdateOrCreateQuerySet.as_manager()

    @classmethod
    def bulk_update_or_create(cls, temperatures):
        """
        Django bulk_create is really fast if you know all records are new.
        Django bulk_update is quick but you need to be sure they all exist.
        
        Used an external package bulk_update_or_create. ref: https://pypi.org/project/django-bulk-update-or-create/
        
        For a batch of records:
         * SELECT all from database (based on the match_field parameter)
         * Update records in memory
         * Use bulk_update for those
         * Use INSERT/.create on each of the remaining
        
        Args:
            list of temperature objects.
        """
        try:
            cls.bulk_objects.bulk_update_or_create(
                temperatures, 
                ['uuid', 'timestamp', 'temperature', 'duration'], 
                match_field='uuid'
            )
        except:
            raise
