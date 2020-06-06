from abc import ABC

from rest_framework import serializers
from .models import Chat


class ChatSerializer(serializers.Serializer):
    chat_id = serializers.IntegerField()
    chat_description = serializers.CharField(max_length=200)
    chat_type = serializers.CharField(max_length=200)
    chat_text = serializers.CharField(max_length=1000)
    date_message = serializers.DateTimeField()
    user_first_name_from = serializers.CharField()
    user_first_name_to = serializers.CharField()

    def create(self, validated_data):
        return Chat.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)

class UserChatSerializer(serializers.Serializer):
    chat_id = serializers.IntegerField()
    chat_description = serializers.CharField(max_length=200)
    chat_type = serializers.CharField(max_length=200)
    chat_text = serializers.CharField(max_length=1000)
    date_message = serializers.DateTimeField()

