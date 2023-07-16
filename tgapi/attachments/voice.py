class Voice:
	def __init__(self, voice):
		self.duration = voice["duration"]
		self.mime_type = voice["mime_type"]
		self.file_id = voice["file_id"]
		self.file_unique_id = voice["file_unique_id"]
		self.file_size = voice["file_size"]
