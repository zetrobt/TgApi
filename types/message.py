class Message:
	def __init__(self, message):
		self.user_id = message["from"]["id"]
		self.chat_id = message["chat"]["id"]
		self.text = message["text"]
