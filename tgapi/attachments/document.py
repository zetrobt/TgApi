class Document:
	def __init__(self, document):
		if "file_name" in document:
			self.file_name = document["file_name"]
		self.mime_type = document["mime_type"]
		self.file_id = document["file_id"]
		self.file_unique_id = document["file_unique_id"]
		self.file_size = document["file_size"]
		if "thumbnail" in document:
			self.thumbnail = document["thumbnail"]
			
