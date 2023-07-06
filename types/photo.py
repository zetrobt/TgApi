class Photo:
	def __init__(self, photo):
		self.file_id = photo["file_id"]
		self.file_unique_id = photo["file_unique_id"]
		self.width = photo["width"]
		self.height = photo["height"]
		
