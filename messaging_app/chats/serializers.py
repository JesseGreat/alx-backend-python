# chats/serializers.py

from rest_framework import serializers
from .models import CustomUser, Message, Conversation
from django.contrib.auth import get_user_model


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['user_id', 'first_name', 'last_name', 'email', 'phone_number', 'role', 'created_at']


class MessageSerializer(serializers.ModelSerializer):
    sender = CustomUserSerializer(read_only=True)  # Nested serializer for sender
    conversation = serializers.PrimaryKeyRelatedField(queryset=Conversation.objects.all())  # Just the primary key for conversation

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'conversation', 'message_body', 'sent_at']


class ConversationSerializer(serializers.ModelSerializer):
    participants = CustomUserSerializer(many=True, read_only=True)  # Nested serializer for participants
    messages = MessageSerializer(many=True, read_only=True)  # Nested serializer for messages in the conversation

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'created_at', 'messages']
