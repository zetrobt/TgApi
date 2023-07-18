from requests import Session, get, post
from time import sleep
from json import dumps
from .attachments import Message, Actions, File
from .handlers import Handler
from .utils import *

class TgApi:
	def __init__(self, token=None):
		self.handlers = []
		self.last_update = 0
		if not token:
			print("Insert bot token!")
			raise SystemExit
		else:
			self.token=token
			self.rq = Session(base_url=f"https://api.telegram.org/bot{token}/")
	
	def polling(self):
		while True:
			updates = self.rq.get(f"getUpdates?offset={self.last_update}").json()["result"]
			print(updates)
			for update in updates:
				self.last_update = int(update["update_id"]) + 1
				if update["message"]:
					message = Message(update["message"])
					for handler in self.handlers:
						if hasattr(message, "text") and message.text == handler.command:
							handler.callback(message)
			sleep(0.25)
	
	def command(self, command=None):
		if not command:
			print("Error! Pass command to handler")
			return
		def new_handler(callback):
			Handler(callback, self, command)
		return new_handler
	
	def _create_handler(self, handler=None, content=False):
		if not handler:
			print("Error! Pass handler to create_handler")
			return
		self.handlers.append(handler)
			
	def send_message(self, chat_id, text, reply_markup=None):
		if not reply_markup:
			return Message(self.rq.get(f"sendMessage?chat_id={chat_id}&text={text}").json()["result"])
		x = Message(self.rq.get(f"sendMessage?chat_id={chat_id}&text={text}&reply_markup={reply_markup}").json()["result"])
		print(x)
	
	def reply_message(self, chat_id, message_id, text, reply_markup=None):
		if not reply_markup:
			return Message(self.rq.get(f"sendMessage?chat_id={chat_id}&text={text}&reply_to_message_id={message_id}").json()["result"])
		return Message(self.rq.get(f"sendMessage?chat_id={chat_id}&text={text}&reply_to_message_id={message_id}&reply_markup={reply_markup}").json()["result"])
	
	def edit_message(self, chat_id, message_id, text):
		self.rq.get(f"editMessageText?chat_id={chat_id}&message_id={message_id}&text={text}")
	
	def forward_message(self, from_chat_id, message_id, chat_id):
		self.rq.get(f"forwardMessage?from_chat_id={from_chat_id}&message_id={message_id}&chat_id={chat_id}")
	
	def send_action(self, chat_id, action):
		self.rq.get(f"sendChatAction?chat_id={chat_id}&action={action}")
	
	def send_photo(self, chat_id, photo, caption=None):
		if not caption:
			return Message(self.rq.post(f"sendPhoto?chat_id={chat_id}", files={'photo': photo}).json()["result"])
		return Message(self.rq.post(f"sendPhoto?chat_id={chat_id}&caption={caption}", files={'photo': photo}).json()["result"])
		
	def send_document(self, chat_id, document, caption=None):
		if not caption:
			return Message(self.rq.post(f"sendDocument?chat_id={chat_id}", files={'document': document}).json()["result"])
		return Message(self.rq.post(f"sendDocument?chat_id={chat_id}&caption={caption}", files={'document': document}).json()["result"])
		
	def send_video(self, chat_id, video, caption=None):
		if not caption:
			return Message(self.rq.post(f"sendVideo?chat_id={chat_id}", files={'video': video}).json()["result"])
		return Message(self.rq.post(f"sendVideo?chat_id={chat_id}&caption={caption}", files={'video': video}).json()["result"])
	
	def send_audio(self, chat_id, audio, caption=None):
		if not caption:
			return Message(self.rq.post(f"sendAudio?chat_id={chat_id}", files={'audio': audio}).json()["result"])
		return Message(self.rq.post(f"sendAudio?chat_id={chat_id}&caption={caption}", files={'audio': audio}).json()["result"])
	
	def send_sticker(self, chat_id, sticker):
		return Message(self.rq.post(f"sendSticker?chat_id={chat_id}", files={'sticker': sticker}).json()["result"])
	
	def send_voice(self, chat_id, voice):
		return Message(self.rq.post(f"sendVoice?chat_id={chat_id}", files={'voice': voice}).json()["result"])
		
	def send_dice(self, chat_id, emoji='🎲'):
		return Message(self.rq.get(f"sendDice?chat_id={chat_id}&emoji={emoji}").json()["result"])
		
	def send_location(self, chat_id, latitude, longitude):
		return Message(self.rq.get(f"sendLocation?chat_id={chat_id}&latitude={latitude}&longitude={longitude}").json()["result"])
	
	def get_file(self, id):
		return File(self.rq.get(f"getFile?file_id={id}").json()["result"])
	
	def download_file(self, path):
		return get(f"https://api.telegram.org/file/bot{self.token}/{path}")
	
	def delete_message(self, chat_id, message_id):
		self.rq.get(f"deleteMessage?chat_id={chat_id}&message_id={message_id}")
	
	def get_me(self):
		return self.rq.get("getMe").json()["result"]
