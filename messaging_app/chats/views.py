from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    # Custom action to create a new conversation
    @action(detail=False, methods=['post'])
    def create_conversation(self, request):
        participants = request.data.get('participants', [])
        if len(participants) < 2:
            return Response({'detail': 'A conversation must have at least two participants.'}, status=400)

        conversation = Conversation.objects.create()
        conversation.participants.set(participants)  # Set the participants as many-to-many relation
        conversation.save()
        return Response(ConversationSerializer(conversation).data, status=201)

        
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    # Custom action to send a new message to a conversation
    @action(detail=True, methods=['post'])
    def send_message(self, request, pk=None):
        conversation = self.get_object()
        sender = request.user  # Assuming the sender is the currently authenticated user
        message_body = request.data.get('message_body')

        if not message_body:
            return Response({'detail': 'Message body is required.'}, status=400)

        # Create a new message for the conversation
        message = Message.objects.create(sender=sender, conversation=conversation, message_body=message_body)
        return Response(MessageSerializer(message).data, status=201)
