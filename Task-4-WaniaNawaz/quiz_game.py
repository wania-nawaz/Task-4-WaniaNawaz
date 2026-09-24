"""
Project 4: The General Knowledge Quiz
DecodeLabs - Python Programming Industrial Training Kit

Description:
    A quiz game that asks the user a series of questions, tracks a
    running score, and reports the final result. Demonstrates control
    flow (if-else), variable/state management, and input sanitization.

Key Skills Demonstrated:
    - If-Else Logic & Control Flow
    - Variable / State Management (score tracking)
    - Input Sanitization (.strip() and .lower())
"""

QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "answer": "paris",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "answer": "mars",
    },
    {
        "question": "What is the largest ocean on Earth?",
        "answer": "pacific",
    },
]


def sanitize_input(raw_text):
    """Clean raw user input by removing whitespace and normalizing case."""
    return raw_text.strip().lower()


def run_quiz(questions):
    """Ask each question in sequence and return the final score."""
    score = 0

    for index, item in enumerate(questions, start=1):
        print(f"\nQ{index}. {item['question']}")
        user_answer = input("Your answer: ")
        cleaned_answer = sanitize_input(user_answer)

        if cleaned_answer == item["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was '{item['answer'].title()}'.")

    return score


def show_result(score, total):
    """Display the final score and a performance message."""
    print("\n" + "=" * 40)
    print(f"Final Score: {score} / {total}")

    if score == total:
        print("Perfect score! Excellent work.")
    elif score >= total / 2:
        print("Good effort! Keep practicing.")
    else:
        print("Better luck next time!")
    print("=" * 40)


def main():
    print("=" * 40)
    print("     DecodeLabs General Knowledge Quiz")
    print("=" * 40)

    final_score = run_quiz(QUESTIONS)
    show_result(final_score, len(QUESTIONS))


if __name__ == "__main__":
    main()
