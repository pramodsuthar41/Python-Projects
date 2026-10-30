questions = [
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["A. function", "B. def", "C. define", "D. fun"],
        "answer": "B"
    },
    {
        "question": "Which data type stores key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!--", "C. #", "D. /*"],
        "answer": "C"
    },
    {
        "question": "Which of the following is a mutable data type?",
        "options": ["A. Tuple", "B. String", "C. List", "D. Integer"],
        "answer": "C"
    },
    {
        "question": "Which function is used to display output in Python?",
        "options": ["A. input()", "B. print()", "C. display()", "D. output()"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to create a class in Python?",
        "options": ["A. object", "B. class", "C. create", "D. def"],
        "answer": "B"
    },
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": ["A. 6", "B. 8", "C. 9", "D. 5"],
        "answer": "B"
    },
    {
        "question": "Which loop is used to iterate over a sequence?",
        "options": ["A. repeat", "B. foreach", "C. for", "D. iterate"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to check a condition?",
        "options": ["A. when", "B. if", "C. check", "D. condition"],
        "answer": "B"
    },
    {
        "question": "Which method adds an element to the end of a list?",
        "options": ["A. add()", "B. insert_end()", "C. append()", "D. push()"],
        "answer": "C"
    },
    {
        "question": "Which data type stores unique elements?",
        "options": ["A. List", "B. Tuple", "C. Set", "D. String"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to return a value from a function?",
        "options": ["A. yield", "B. return", "C. break", "D. pass"],
        "answer": "B"
    }
]

score = 0

print("=" * 40)
print("WELCOME TO QUIZ")
print("=" * 40)

for question in questions:
    print("\n" + question["question"])

    for option in question["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D).").strip().upper()

    while user_answer not in ["A", "B", "C", "D"]:
        print("Invalid input! Please enter A, B, C or D.")
        user_answer = input("Enter your answer.").strip().upper()

    if user_answer == question["answer"]:
        print("Correct Answer")
        score += 1
    else:
        print("Wrong Answer!")
        print("Correct answer:", question["answer"])

total_questions = len(questions)
percentage = (score/total_questions) * 100


print("\n" + "=" * 40)
print("QUIZ RESULTS")
print("=" * 40)

print("Total Questions:", total_questions)
print("Correct Answers:", score)
print("Wrong Answers:", total_questions - score)
print("Final Score:", str(score) + "/" + str(total_questions))
print("Percentage:", round(percentage, 2), "%")

if percentage >= 80:
    print("Excellent performance!")
elif percentage >= 60:
    print("Good job!")
elif percentage >= 40:
    print("Keep practicing!")
else:
    print("Don't give up! Try again.")

print("=" * 40)
