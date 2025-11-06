print("Quicky Study Quizzy")

score = 0 
total_questions = 0

total_questions += 1
print("Question 1: Whats is 7 x 8?")
answer = input("Your answer: ")

if answer == "56":
    print("Perfectly done! \n")
    score += 1
else:
    print("Nuh uh bruda. Try again! \n")

total_questions += 1
print("Question 2: What is the capital of Slovakia?")
answer = input("Your answer: ").lower()

if answer == "Bratislava":
    print("Keep it up!\n")
    score += 1
elif answer == "bratislava":
    print ("Keep it up!")
    score += 1
else:
    print("Nuh uh try again")

total_questions += 1
print("Question 3: How many continents are there?")
answer = input("Your answer: ")
print(f"DEBUG: You typed'{answer}' (length: {len(answer)})")
if answer == "7":
    print("Hell yeah!\n")
    score += 1
else:
    print("Nuh uh try again :P")

percentage = (score / total_questions) * 100

print("="*50)
print(f"You scored {score}/{total_questions} ({percentage:.1f}%)")

if percentage == 100:
    print("Perfekcion bruda")
elif percentage >= 70:
    print("Good job it doesn't need perfection!")
elif percentage >= 50:
    print("Keep it up!!!")
else:
    print("We all started from scratch, keep going!")
print("="*50)
