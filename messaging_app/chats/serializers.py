from rest_framework import serializers
from .models import CustomUser, Message, Conversation
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, SerializerMethodField


# User Serializer
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['user_id', 'first_name', 'last_name', 'email', 'phone_number', 'role', 'created_at']


# Message Serializer
class MessageSerializer(serializers.ModelSerializer):
    sender = CustomUserSerializer(read_only=True)  # Nested serializer for sender
    conversation = serializers.PrimaryKeyRelatedField(queryset=Conversation.objects.all())  # Just the primary key for conversation

    # Adding a SerializerMethodField for a custom computed field
    message_preview = SerializerMethodField()

    def get_message_preview(self, obj):
        # This method will return a preview of the message body (first 50 characters)
        return obj.message_body[:50]  # Limiting to first 50 characters as a preview

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'conversation', 'message_body', 'sent_at', 'message_preview']


# Conversation Serializer
class ConversationSerializer(serializers.ModelSerializer):
    participants = CustomUserSerializer(many=True, read_only=True)  # Nested serializer for participants
    messages = MessageSerializer(many=True, read_only=True)  # Nested serializer for messages in the conversation

    # Adding a custom validation to ensure there is at least one participant in the conversation
    def validate_participants(self, value):
        if len(value) < 2:
            raise ValidationError("A conversation must have at least two participants.")
        return value

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'created_at', 'messages']
