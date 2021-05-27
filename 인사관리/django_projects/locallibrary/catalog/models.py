from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances


class Person(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    이름 = models.CharField(max_length=255, blank=True, null=True)
    나이= models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'
