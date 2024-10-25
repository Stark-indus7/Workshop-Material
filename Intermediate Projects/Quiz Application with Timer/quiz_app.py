# This is the main Python file for the Quiz Application with Timer project.
import time

questions = {
    "What is the capital of France?": "Paris",
    "Who wrote 'Harry Potter'?": "J.K. Rowling",
    "What is the square root of 64?": "8"
}

def quiz():
    score = 0
    for question, answer in questions.items():
        print(f"\n{question}")
        start_time = time.time()
        user_answer = input("Your answer: ")
        end_time = time.time()
        if (end_time - start_time) <= 10:  # 10 seconds to answer
            if user_answer.lower() == answer.lower():
                score += 1
                print("Correct!")
            else:
                print("Wrong answer!")
        else:
            print("Time's up!")

    print(f"\nYour final score is {score}/{len(questions)}.")

quiz()
