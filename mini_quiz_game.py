questions = [
    ("What is the capital of France?", "Paris"),
    ("How many continents are there?", "7"),
    ("What is 2+2?", "4"),
    ("Which planet is known as the Red Planet?", "Mars"),
    ("Who painted the Mona Lisa?", "Leonardo da Vinci")
]

score = 0
print("Welcome to the Quiz Game!\n")

for i, (question, answer) in enumerate(questions, 1):
    user_answer = input(f"Q{i}: {question}\nYour Answer: ")
    if user_answer.lower() == answer.lower():
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The answer is {answer}\n")

print(f"Final Score: {score}/{len(questions)}")
if score == len(questions): print("Perfect! ")
elif score >= len(questions)/2: print("Good job!")
else: print("Keep practicing!")