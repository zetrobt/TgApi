from .photo import Photo
from .document import Document
from .video import Video
from .audio import Audio
from .sticker import Sticker
from .voice import Voice
from .dice import Dice
from .location import Location
from .poll import Poll
from .video_note import VideoNote
from .venue import Venue

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
		if "reply_to_message" in message:
			self.reply_to_message = Message(message["reply_to_message"])
		if "location" in message:
			self.location = Location(message["location"])
		if "poll" in message:
			self.poll = Poll(message["poll"])
		if "video_note" in message:
			self.video_note = VideoNote(message["video_note"])
		if "venue" in message:
			self.venue = Venue(message["venue"])