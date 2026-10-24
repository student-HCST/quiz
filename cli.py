# CLI Quiz Application in Python

questions = [
    {
        "question": "1. Which language is used for Python programming?",
        "options": ["A. HTML", "B. Python", "C. CSS", "D. SQL"],
        "answer": "B"
    },
    {
        "question": "2. Which data type stores whole numbers in Python?",
        "options": ["A. str", "B. float", "C. int", "D. list"],
        "answer": "C"
    },
    {
        "question": "3. Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. <!--", "D. **"],
        "answer": "B"
    },
    {
        "question": "4. Which function displays output in Python?",
        "options": ["A. input()", "B. print()", "C. show()", "D. display()"],
        "answer": "B"
    },
    {
        "question": "5. Which keyword is used for a loop in Python?",
        "options": ["A. repeat", "B. loop", "C. for", "D. iterate"],
        "answer": "C"
    }
]

score = 0
total = len(questions)

print("================================")
print("      WELCOME TO QUIZ GAME")
print("================================")

name = input("Enter your name: ")

print("\nHello,", name)
print("Each correct answer gives 1 mark.")
print("Enter A, B, C, or D to answer.\n")

for q in questions:
    print(q["question"])

    for option in q["options"]:
        print(option)

    while True:
        user_answer = input("Your answer: ").strip().upper()

        if user_answer in ["A", "B", "C", "D"]:
            break

        print("Invalid choice! Please enter A, B, C, or D.")

    if user_answer == q["answer"]:
        print("Correct answer!\n")
        score = score + 1
    else:
        print("Wrong answer!")
        print("Correct answer:", q["answer"], "\n")

percentage = (score / total) * 100

print("================================")
print("          QUIZ RESULT")
print("================================")
print("Name:", name)
print("Total Questions:", total)
print("Correct Answers:", score)
print("Wrong Answers:", total - score)
print("Final Score:", score, "/", total)
print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Excellent performance!")
elif percentage >= 50:
    print("Good job! Keep practicing.")
else:
    print("Keep learning and try again!")

print("Thank you for playing!")