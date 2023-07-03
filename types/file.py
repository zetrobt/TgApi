class File:
	def __init__(self, file):
		self.id = file["file_id"]
		self.unique_id = file["file_unique_id"]
		self.size = file["file_size"]
		self.path = file["file_path"]
