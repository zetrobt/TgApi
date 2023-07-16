class Video:
	def __init__(self, video):
		self.duration = video["duration"]
		self.width = video["width"]
		self.height = video["height"]
		self.mime_type = video["mime_type"]
		self.thumbnail = video["thumbnail"]
		self.thumb = video["thumb"]
