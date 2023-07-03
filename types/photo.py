class Photo:
	def __init__(self, photo):
		self.small_size_id = photo[0]["file_id"]
		self.normal_size_id = photo[1]["file_id"]
		self.large_size_id = photo[2]["file_id"]
