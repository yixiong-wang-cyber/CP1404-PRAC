"""Determine the status of a user-entered score and a random score."""

import random


def main():
    """Get a user score and a random score, then print their results."""
    score = float(input("Enter score: "))
    result = determine_score(score)
    print(f"User score {score} is {result}")
    if result == "Excellent":
        print("You get a prize!")

    random_score = random.randint(0, 100)
    random_result = determine_score(random_score)
    print(f"Random: {random_score} = {random_result}")


def determine_score(score):
    """Determine the result for a score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
