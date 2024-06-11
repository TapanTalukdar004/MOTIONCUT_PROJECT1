# Define a function to display questions and capture user input
def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    
    while True:
        try:
            answer = int(input("Please select an option (1-4): "))
            if 1 <= answer <= len(options):
                break
            else:
                print("Invalid option. Please select a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    return answer == correct_answer

# Define the main function to run the quiz
def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Madrid"],
            "correct_answer": 1
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "correct_answer": 2
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "correct_answer": 4
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["Harper Lee", "J.K. Rowling", "Ernest Hemingway", "Mark Twain"],
            "correct_answer": 1
        },
        {
            "question": "What is the square root of 64?",
            "options": ["6", "7", "8", "9"],
            "correct_answer": 3
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"],
            "correct_answer": 2
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["O2", "H2O", "CO2", "NaCl"],
            "correct_answer": 2
        },
        {
            "question": "Which country is known as the Land of the Rising Sun?",
            "options": ["China", "Japan", "Thailand", "India"],
            "correct_answer": 2
        },
        {
            "question": "What is the capital city of Australia?",
            "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
            "correct_answer": 3
        },
        {
            "question": "Who discovered penicillin?",
            "options": ["Marie Curie", "Alexander Fleming", "Isaac Newton", "Albert Einstein"],
            "correct_answer": 2
        }
    ]
    
    score = 0
    
    for q in questions:
        if ask_question(q["question"], q["options"], q["correct_answer"]):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['options'][q['correct_answer'] - 1]}")
        print()
    
    print(f"Your final score is {score} out of {len(questions)}")

# Run the quiz
if __name__ == "__main__":
    run_quiz()
