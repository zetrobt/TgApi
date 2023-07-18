class VideoNote:
	def __init__(self, video_note):
		self.duration = video_note["duration"]
		self.length = video_note["length"]
		self.thumbnail = video_note["thumbnail"]
		self.thumb = video_note["thumb"]
		self.file_id = video_note["file_id"]
		self.file_unique_id = video_note["file_unique_id"]
		self.file_size = video_note["file_size"]