from requests import Session, get
from time import sleep
from json import dumps
from .types import Message, Actions
from .handlers import Handler
from .utils import *

class TgApi:
	def __init__(self, token=None):
		self.handlers = []
		self.last_update = 0
		if not token:
			print("Insert bot token!")
			raise SystemError
		else:
			self.token=token
			self.rq = Session(base_url=f"https://api.telegram.org/bot{token}/")
	
	def _exec_task(self, task, *args, **kwargs):
	           task(*args, **kwargs)
	
	def polling(self, infinity=False):
		while True:
			updates = self.rq.get(f"getUpdates?offset={self.last_update}").json()["result"]
			print(updates)
			for update in updates:
				#print(update)
				if update["message"]:
					message = Message(update["message"])
					for handler in self.handlers:
						if message.text == handler.command:
							self.last_update = int(update["update_id"]) + 1
							handler.callback(message)
			sleep(0.25)
	
	def handler(self, command=None):
		if not command:
			print("Error! Pass command to handler")
			return
		def new_handler(callback):
			Handler(callback, self, command)
		return new_handler
	
	def _create_handler(self, handler=None):
		if not handler:
			print("Error! Pass handler to create_handler")
			return
		self.handlers.append(handler)
	
	def send_message(self, chat_id, text, reply_markup=None):
		if not reply_markup:
			return Message(self.rq.get(f"sendMessage?chat_id={chat_id}&text={text}").json()["result"])
		return Message(self.rq.get(f"sendMessage?chat_id={chat_id}&text={text}&reply_markup={reply_markup}").json()["result"])
	
	def reply_message(self, message, text, reply_markup=None):
		if not reply_markup:
			return Message(self.rq.get(f"sendMessage?chat_id={message.chat_id}&text={text}&reply_to_message_id={message.id}").json()["result"])
		return Message(self.rq.get(f"sendMessage?chat_id={message.chat_id}&text={text}&reply_to_message_id={message.id}&reply_markup={reply_markup}").json()["result"])
	
	def edit_message(self, chat_id, message_id, text):
		self.rq.get(f"editMessageText?chat_id={chat_id}&message_id={message_id}&text={text}")
	
	def forward_message(self, from_chat_id, message_id, chat_id):
		self.rq.get(f"forwardMessage?from_chat_id={from_chat_id}&message_id={message_id}&chat_id={chat_id}")
	
	def send_action(self, chat_id, action):
		self.rq.get(f"sendChatAction?chat_id={chat_id}&action={action}")
