from django.db import models
class Userinfo(models.Model):
    user_num = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userinfo'
# Create your models here.
