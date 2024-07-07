

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! The correct answer was", question["answer"], "\n")
    print(f"You got {score} out of {len(questions)} questions correct.")

questions = [
    {
        "prompt": "What is the capital of UK?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "B"
    },
    {
        "prompt": "Which language is primarily spoken in France?",
        "options": ["A. Spanish", "B. Portuguese", "C. English", "D. French"],
        "answer": "D"
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    },
    {
        "prompt": "Who wrote 'Harry Potter'?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
        "answer": "C"
    }
]

# Run the quiz
run_quiz(questions)
