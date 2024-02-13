import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question['text'])
        for i, option in enumerate(question['options'], start=1):
            print(f"{i}. {option}")
        user_answer = self.get_user_input(len(question['options']))
        self.check_answer(question, user_answer)

    def get_user_input(self, max_options):
        while True:
            try:
                user_input = int(input(f"Enter your choice (1-{max_options}): "))
                if 1 <= user_input <= max_options:
                    return user_input
                else:
                    print("Invalid choice. Please enter a number within the given range.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def check_answer(self, question, user_answer):
        correct_answer = question['answer']
        if user_answer == correct_answer:
            print("Correct!")
            self.score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}: {question['options'][correct_answer - 1]}")

    def start_quiz(self):
        print("Welcome to the Quiz Game!\n")
        for question in self.questions:
            self.display_question(question)
            print()

        print(f"Quiz Completed! Your final score is: {self.score}/{len(self.questions)}")

# Example questions. You can customize these.
questions = [
    {
        'text': 'What is the capital of France?',
        'options': ['Paris', 'Berlin', 'London', 'Rome'],
        'answer': 1
    },
    {
        'text': 'Which programming language is known for its readability?',
        'options': ['Python', 'Java', 'C++', 'Ruby'],
        'answer': 1
    },
    {
        'text': 'What is the largest mammal?',
        'options': ['Elephant', 'Blue Whale', 'Giraffe', 'Hippopotamus'],
        'answer': 2
    }
]

# Shuffle the questions to make the quiz more dynamic
random.shuffle(questions)

# Create and start the quiz
quiz = QuizGame(questions)
quiz.start_quiz()
