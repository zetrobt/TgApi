class Venue:
	def __init__(self, venue):
		self.latitude = venue["location"]["latitude"]
		self.longitude = venue["location"]["longitude"]
		self.title = venue["title"]
		self.address = venue["address"]