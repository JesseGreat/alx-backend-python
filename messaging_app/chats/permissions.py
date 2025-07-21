from rest_framework import permissions, BasePermission
# chats/permissions.py

from .models import Conversation

class IsParticipantOfConversation(BasePermission):
    """
    Custom permission to check if the user is a participant in the conversation.
    """
    
    def has_object_permission(self, request, view, obj):
        """
        Check if the user is a participant in the conversation.
        The obj will be the Message or Conversation instance.
        """
        if isinstance(obj, Conversation):
            # If the object is a conversation, check if the user is a participant
            return request.user in obj.participants.all()
        
        if isinstance(obj, Message):
            # If the object is a message, check if the user is part of the conversation the message belongs to
            return request.user in obj.conversation.participants.all()

        return False
