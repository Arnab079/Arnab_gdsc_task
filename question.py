class Question:
	def __init__(self, text, answer):
	self.text = text
	self.answer = answer

	def is_right(self, response):
		return response = self.answer