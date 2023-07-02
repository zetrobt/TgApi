from requests import get
from time import sleep
from .types.message import Message

class TgApi:
	def __init__(self, token=None):
		self.handlers = []
		self.last_update = 0
		if not token:
			print("Insert bot token!")
			raise SystemError
		else:
			self.token=token
	
	def _exec_task(self, task, *args, **kwargs):
	           task(*args, **kwargs)
	
	def polling(self, infinity=False):
		while True:
			updates = get(f"https://api.telegram.org/bot{self.token}/getUpdates?offset={self.last_update}").json()["result"]
			for update in updates:
				#print(update)
				if update["message"]:
					message = Message(update["message"])
					for handler in self.handlers:
						if message.text == handler.command:
							self.last_update = int(update["update_id"]) + 1
							handler.callback(message)
			sleep(0.25)
	
	def create_handler(self, handler=None):
		if not handler:
			print("Error! Pass handler to create_handler")
			return
		self.handlers.append(handler)
	
	def send_message(self, chat_id, text):
	           get(f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={chat_id}&text={text}")
