#: A simple multiple choice quiz, implementing the oop.

from Question_class import Question

# List of questions and answer choices
questions_prompt  = [
    "1. What color are apples?\n (a) Red\n (b) Green\n (c) Orange\n",
    "2. What color are bananas?\n (a) Red\n (b) Yellow\n (c) Orange\n",
    "3. What color are strawberries?\n (a) Red\n (b) Green\n (c) Orange\n"
    ]

# Creating a question objects using the class
questions = [
    Question(questions_prompt[0], "a"),
    Question(questions_prompt[1], "b"),
    Question(questions_prompt[2], "a")
    ]

# A function that will ask answer and tracks the score
def run_test(questions):
    score = 0
    
    for question in questions:
        user_ans = input(question.prompt)
        if user_ans == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.")
    
run_test(questions)
