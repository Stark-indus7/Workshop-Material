
import movie as m


def load_questions():
    return [
        {"question":" 1st Prime minister of India",
         "options": ["1. J.P Nadda","2. Pt. Jawaharlal Nehru","3. Sardar Vallabh Bhai Patel","4. Mahatma Gandhi"],
         "answer":"2"},
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

def ask_question(questions_dict):
    print("\n" + questions_dict["question"])
    
    for option in questions_dict["options"]:
        print(option)
    while True:
        try:
            answer = input("Enter your answer (1/2/3/4): ")
            if answer in ["1","2","3","4"]:
                return answer
            else:
                print("Invalid Answer Please type in 1,2,3,4")
        except Exception as e:
            print(e)

def simple_quiz():
    print("Welcome to Pyaare Quiz Competition!")
    questions = load_questions()
    score = 0

    for q in questions:
        usr_ans = ask_question(q)
        if usr_ans == q["answer"]:
            print("Yay! Your answer is correct!")
            score += 1
        else:
            correct_ans = q["options"][int(q["answer"])-1]
            print(f"Oh! Sorry but the answer was {correct_ans}")
    # print(score)
    print(f"Your score : {score} Out of questions : {len(questions)}")
    percentage = (score/len(questions))*100
    print(f"Your percentage is : {percentage}%")




simple_quiz()


