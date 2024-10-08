def load_questions():
    """Load quiz questions."""
    return [
        {
            "question": "What is the capital of France?",
            "options": ["1. Berlin", "2. London", "3. Paris", "4. Madrid"],
            "answer": "3"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["1. Earth", "2. Mars", "3. Jupiter", "4. Venus"],
            "answer": "2"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["1. Harper Lee", "2. Mark Twain", "3. Jane Austen", "4. Charles Dickens"],
            "answer": "1"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["1. Atlantic Ocean", "2. Indian Ocean", "3. Arctic Ocean", "4. Pacific Ocean"],
            "answer": "4"
        },
        {
            "question": "What is the chemical symbol for Gold?",
            "options": ["1. Au", "2. Ag", "3. Gd", "4. Go"],
            "answer": "1"
        }
    ]

def ask_question(question_dict):
    """Ask a single quiz question."""
    print("\n" + question_dict["question"])
    for option in question_dict["options"]:
        print(option)
    
    while True:
        answer = input("Enter the number of your answer: ")
        if answer in ['1', '2', '3', '4']:
            return answer
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

def main():
    """Main function to run the Quiz Game."""
    print("Welcome to the Quiz Game!")
    questions = load_questions()
    score = 0
    
    for q in questions:
        user_answer = ask_question(q)
        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            correct_option = q["options"][int(q["answer"]) - 1]
            print(f"Wrong. The correct answer is {correct_option}.\n")
    
    print(f"Quiz Completed! Your Score: {score} out of {len(questions)}")
    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage}%")
    
    if percentage == 100:
        print("Excellent work!")
    elif percentage >= 60:
        print("Good job!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
