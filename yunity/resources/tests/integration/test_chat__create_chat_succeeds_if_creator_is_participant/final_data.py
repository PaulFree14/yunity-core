from yunity.conversations.models import Conversation

assert Conversation.objects.count() == 1, 'chat object was not created'
