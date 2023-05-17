# Imports
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# List of Question objects (empty at first)
question_bank = []

# For loop to add Questions to question bank
for q in question_data:
    new_question = Question(q['text'], q['answer'])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()