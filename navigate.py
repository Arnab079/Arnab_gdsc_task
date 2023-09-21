from question import Question
from 



class Navigate:
	def__innit__(self, question_List):
		self.question_List = question_List
		self.score = 0
		self.question_number = 0


	def next_question(self):
		if self.question_number < len(self.question_List):
			question = self.question_List[self.question_number]
			self.question_number += 1
			return question

		else :
			return None


	def check_answer(self, response):
		on_question = self.question_List[self.question_number - 1 ]
		if on_question.is_right(response):
			self.score += 2
		else :
			self.score += -1

	def if_question_left(self):
		return self.question_number< len(self.question_List)



