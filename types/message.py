from .photo import Photo
from .document import Document
from .video import Video
from .audio import Audio
from .sticker import Sticker
from .voice import Voice
from .dice import Dice

class Message:
	def __init__(self, message):
		print(message)
		self.id = message["message_id"]
		self.user_id = message["from"]["id"]
		self.chat_id = message["chat"]["id"]
		if "text" in message:
			self.text = message["text"]
		if "caption" in message:
			self.text = message["caption"]
		if "photo" in message:
			self.photo = [Photo(x) for x in message["photo"]]
		if "document" in message:
			self.document = Document(message["document"])
		if "video" in message:
			self.video = Video(message["video"])
		if "audio" in message:
			self.audio = Audio(message["audio"])
		if "sticker" in message:
			self.sticker = Sticker(message["sticker"])
		if "voice" in message:
			self.voice = Voice(message["voice"])
		if "dice" in message:
			self.dice = Dice(message["dice"])
			
