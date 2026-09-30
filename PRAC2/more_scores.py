"""Generate random scores and write their results to a file."""

import random


def main():
    """Generate a number of random scores and write results to results.txt."""
    number_of_scores = int(input("Enter number of scores: "))
    with open("results.txt", "w") as out_file:
        for _ in range(number_of_scores):
            score = random.randint(0, 100)
            result = determine_score(score)
            out_file.write(f"{score} is {result}\n")


def determine_score(score):
    """Determine the result for a score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
