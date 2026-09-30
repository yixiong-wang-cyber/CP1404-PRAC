"""Menu program for getting a valid score and working with it."""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""
MIN_SCORE = 0
MAX_SCORE = 100


def main():
    """Display a menu and handle the user's choices until they quit."""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


def get_valid_score():
    """Get a valid score between MIN_SCORE and MAX_SCORE inclusive."""
    score = int(input(f"Enter score ({MIN_SCORE}-{MAX_SCORE}): "))
    while score < MIN_SCORE or score > MAX_SCORE:
        print("Invalid score")
        score = int(input(f"Enter score ({MIN_SCORE}-{MAX_SCORE}): "))
    return score


def determine_score(score):
    """Determine the result for a score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_result(score):
    """Print the result for score."""
    print(f"The result for {score} is {determine_score(score)}")


def show_stars(score):
    """Print as many stars as score."""
    print("*" * score)


main()
