from django.db import models
from uuid import uuid4
from datetime import datetime

def get_file_path(instance, file):
    ymd_path = datetime.now().strftime('%Y/%m/%d')
    uuid_name = uuid4().hex
    return '/'.join(['upload_file/', ymd_path, uuid_name])



# Create your models here.
class UploadFileModel(models.Model):
    title = models.TextField(default='')
    file = models.FileField(upload_to=get_file_path,null=True)

    class Meta:
        app_label = "file_save"
        managed = False
        db_table = 'suggestion_uploadfilemodel'


class Userinfo(models.Model):
    user_num = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=32, blank=True, null=True)
    user_password = models.CharField(max_length=64, blank=True, null=True)
    user_name = models.CharField(max_length=12, blank=True, null=True)
    user_phone = models.CharField(max_length=12, blank=True, null=True)
    user_address = models.CharField(max_length=64, blank=True, null=True)
    user_department = models.CharField(max_length=30, blank=True, null=True)
    user_position = models.CharField(max_length=30, blank=True, null=True)
    user_rank = models.IntegerField(blank=True, null=True)
    user_profile = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    user_age = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        app_label = "default"
        db_table = 'userinfo'
class Suggestion(models.Model):
    num = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    sender = models.IntegerField()
    reciever = models.IntegerField()
    status = models.IntegerField()
    file = models.TextField()
    sender_name = models.CharField(max_length=50, blank=True, null=True)
    file_locate = models.IntegerField(blank=True, null=True)
    reciever_name = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        managed = False
        app_label = "default"
        db_table = 'suggestion'

