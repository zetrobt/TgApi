class Chat:
	def __init__(self, chat):
		self.id = chat["id"]
		self.first_name = chat["first_name"]
		if "last_name" in chat:
			self.last_name = chat["last_name"]
		if "username" in chat:
			self.username = chat["username"]
		self.type = chat["type"]
		if "active_usernames" in chat:
			self.active_usernames = chat["active_usernames"]
		if "bio" in chat:
			self.bio = chat["bio"]
		if "photo" in chat:
			self.photo = chat["photo"]