class Poll:
	def __init__(self, poll):
		self.id = poll["id"]
		self.question = poll["question"]
		self.options = poll["options"]
		self.voter_count = poll["total_voter_count"]
		self.is_closed = poll["is_closed"]
		self.is_anonymous = poll["is_anonymous"]
		self.type = poll["type"]
		self.allows_multiple_answers = poll["allows_multiple_answers"]