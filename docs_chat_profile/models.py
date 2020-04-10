from django.db import models


class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    chat_description = models.CharField(max_length=200)
    chat_type = models.CharField(max_length=200)
    chat_text = models.TextField()
    date_message = models.DateTimeField('date send')


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


