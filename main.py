quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Who wrote 'Harry Potter'?",
        "options": ["J.R.R. Tolkien", "J.K. Rowling", "George R.R. Martin", "Stephen King"],
        "answer": "J.K. Rowling"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Jupiter", "Saturn", "Neptune"],
        "answer": "Jupiter"
    },

    {
        "question": "Who is first prophet of islam?",
        "options": ["Saleh(a.s)", "Muhammad (s.a.w)", "Adam(a.s)", "Isa(a.s)"],
        "answer": "Adam(a.s)"
    },

    {
        "question": "Who is father of genetics?",
        "options": ["Robert hook", "Einstein", "Darwin", "Mendel"],
        "answer": "Darwin"
    }



    
 ]

def display_question(question):
    print(question["question"])
    for index,option in enumerate(question["options"],start=1):
        print(f"{index}.{option}")

    user_answer = input("Enter the number of your answer:")
    return user_answer

def run_quiz():
    score = 0
    for question in quiz_questions:
        user_answer = display_question(question)
        if user_answer.lower() == question["answer"].lower():
            print("Correct!\n")
            score +=1

        else:
            print(f"Wrong! The correct answer is :  {question['answer']}\n")

    print(f"You scored {score} out of {len(quiz_questions)}")

if __name__ == "__main__":
    run_quiz()
