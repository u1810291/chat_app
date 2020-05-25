from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    chat_description = models.CharField(max_length=200)
    chat_type = models.CharField(max_length=200)
    chat_text = models.TextField()
    date_message = models.DateTimeField()
    user_first_name_from = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    user_first_name_to = models.IntegerField(default='')


class Groups(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_description = models.CharField(max_length=200)
    group_type = models.CharField(max_length=200)
    group_text = models.TextField()
    group_date_message = models.DateTimeField('date send')


class Smiles(models.Model):
    smile_id = models.AutoField(primary_key=True)
    smile_img = models.ImageField(upload_to='images/')
    smile_date_message = models.DateTimeField('date send')
