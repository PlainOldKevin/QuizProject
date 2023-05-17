class QuizBrain:

    # Init method
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.question_list = question_list

    # Function to get next question and display it to the user
    def next_question(self):
        # Get first question in question bank
        current_question = self.question_list[self.question_number]
        # Increase question number
        self.question_number += 1
        # Prompt user
        input(f"Q.{self.question_number}: {current_question.text} (True/False): ")