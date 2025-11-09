def ask_question(question_text, correct_answer, points=1):
    """
    Ask a question and check if answer is correct.
    Returns: points earnet (points if correct, 0 if wrong)
    """
    print(question_text)
    answer = input("Group answer: ").strip().lower()

    if answer == correct_answer.lower():
        print(f"Correct! ={points} points!\n")
        return points
    else:
        print(f"Not quite. The correct answer is: {correct_answer}\n")
        return 0

def calculate_percentage(score, max_score):
    """Calculate percentage from score"""
    return (score / max_score) * 100
def give_group_feedback(percentage, group_name):
    """Give personalized feedback based on group performance"""
    print("="*60)
    print(f"{group_name.upper()} - RESULTS")
    print("="*60)

    if percentage == 100:
        return "Perfect! You did so well!"
    elif percentage >=75:
        return "Excellent teamwork! Keep it up!"
    elif percentage >=50:
        return "Good effort! Still need a bit revising tho"
    else:
        return "Keep it up! I know it's hard but that shouldn't stop you!"

def run_group_quiz():
    """Run the complete group quiz"""
    print("GROUP STUDY QUIZZO \n")

    group_name = input("What's your group's name? ")
    num_members = int(input("How many of ya're participating today?"))

    print(f"nGreat! {group_name} with {num_members} members, let's begin!\n")

    score = 0
    max_score = 0

    max_score += 1
    score += ask_question(
        "Q1: What is the capital of Japan?",
        "Tokyo",
        points=1    
    )

    max_score += 1
    score += ask_question(
        "Q2: How many continents are there?",
        "7",
        points=1
    )
    max_score +=2
    score += ask_question(
        f"Q3: If each of your {num_members} members studies 3 hours, what's the total? (BONUS: 2 pts)",
        str(num_members * 3),
        points=2
    )
    max_score +=1
    score += ask_question(
        "Q4: What programming language are you learning right now?",
        "Python",
        points=1
    )
    percentage = calculate_percentage(score, max_score)
    feedback = give_group_feedback(percentage, group_name)

    print(f"Final score: {score}/{max_score} points({percentage:.1f}%)")
    print(feedback)

    print(f"\n Tip for {group_name}:")
    if percentage >= 75:
        print("Your group is doing great!Try teaching these concepts to others!")
    else:
        print("Schedule a review session. Teaching each other strenghtens understanding!")
    
    print("="*60)

def ask_to_play_again():
    """Ask if group wants another round"""
    response = input("\nWould your group like to try again? (y/n): ")
    return response.lower() == 'y'

def main():
    play = True
    round_num = 1

    while play:
        if round_num > 1:
            print(f"\n\nROUND {round_num} \n")
        
        run_group_quiz()
        round_num += 1
        play = ask_to_play_again()
    
    print("\nThanks for studying together! keep up the awesome group work!")

main() 