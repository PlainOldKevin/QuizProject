class QuizBrain:

    # Init method
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    # Function to get next question and display it to the user
    def next_question(self):
        # Get first question in question bank
        current_question = self.question_list[self.question_number]
        # Increase question number
        self.question_number += 1
        # Prompt user
        ans = input(f"Q.{self.question_number}: {current_question.text} (T/F)?: ")
        # Check answer
        self.check_answer(ans, current_question.answer)

    # Function to check if quiz is completed or not
    def still_has_questions(self):
        # Check if questions remaining
        return self.question_number < len(self.question_list)
    
    # Function to check user's answer
    def check_answer(self, ans, correct_ans):
        # If user answer is true
        if ans.lower() == correct_ans.lower():
            print("Correct!")
            self.score += 1
        # If user answer is false
        else:
            print("That is incorrect.")
        # Print correct answer and score anyway
        print(f"The correct answer was: {correct_ans}")
        print(f"Your current score is {self.score}/{self.question_number}\n")
