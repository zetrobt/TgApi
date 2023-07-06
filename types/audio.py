class Audio:
	def __init__(self, audio):
		self.duration = audio["duration"]
		self.file_name = audio["file_name"]
		self.mime_type = audio["mime_type"]
		self.title = audio["title"]
		self.performer = audio["performer"]
		self.file_id = audio["file_id"]
		self.file_unique_id = audio["file_unique_id"]
		self.file_size = audio["file_size"]
