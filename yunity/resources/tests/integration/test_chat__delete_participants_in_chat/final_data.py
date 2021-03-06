from yunity.conversations.models import Conversation
from .initial_data import chatid, original_number_of_participants

chat = Conversation.objects.get(id=chatid)
assert chat.participants.count() == original_number_of_participants - 1, "Participant was not deleted"
