from navigate import Navigate
from list import question_List


Quiz = Navigate(question_List)

while Quiz.if_question_left():
	on_question = Quiz.next_question()
	print(on_question.ques)
	response = input("Enter wether True/False:")
	Quiz.check_answer(response)

print(f"Your final score is: {Quiz.score}" )