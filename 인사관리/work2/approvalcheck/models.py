from django.db import models

# Create your models here.

class Suggestions(models.Model):
    id = models.AutoField(primary_key=True) # Field name made lowercase.
    title = models.CharField(max_length=255, blank=True, null=True)
    sender = models.IntegerField(blank=True, null=True)
    receiver = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'suggestions'
        app_label= "default"

class Person(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    이름 = models.CharField(max_length=255, blank=True, null=True)
    나이 = models.IntegerField(blank=True, null=True)
    직급 = models.CharField(max_length=255, blank=True, null=True)
    부서 = models.CharField(max_length=255, blank=True, null=True)
    rank = models.IntegerField(db_column='Rank', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'
        app_label = "userinfo"
