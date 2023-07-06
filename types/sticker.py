class Sticker:
	def __init__(self, sticker):
		self.width = sticker["width"]
		self.height = sticker["height"]
		self.emoji = sticker["emoji"]
		self.is_animated = sticker["is_animated"]
		self.is_video = sticker["is_video"]
		self.type = sticker["type"]
		self.thumbnail = sticker["thumbnail"]
		self.thumb = sticker["thumb"]
