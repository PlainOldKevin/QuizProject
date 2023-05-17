# Imports
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# List of Question objects (empty at first)
question_bank = []

# For loop to add Questions to question bank
for q in question_data:
    new_question = Question(q['question'], q['correct_answer'])
    question_bank.append(new_question)

# Create quiz for user to interact with
quiz = QuizBrain(question_bank)

# Iterate through questions
while quiz.still_has_questions():
    quiz.next_question()

# Ending message
print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{len(quiz.question_list)}")