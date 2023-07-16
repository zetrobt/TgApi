class Handler:
	def __init__(self, callback, api, command):
		self.callback = callback
		self.command = command
		api._create_handler(self)
