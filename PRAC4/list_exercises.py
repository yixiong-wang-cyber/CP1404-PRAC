"""
CP1404/CP5632 Practical
List exercises
"""


def main():
    """Run number statistics and the username security checker."""
    numbers = get_numbers()
    display_number_statistics(numbers)
    check_username()


def get_numbers():
    """Prompt the user for 5 numbers and return them in a list."""
    numbers = []
    for i in range(5):
        number = int(input("Number: "))
        numbers.append(number)
    return numbers


def display_number_statistics(numbers):
    """Display statistics about the list of numbers."""
    print("The first number is", numbers[0])
    print("The last number is", numbers[-1])
    print("The smallest number is", min(numbers))
    print("The largest number is", max(numbers))
    print("The average of the numbers is", sum(numbers) / len(numbers))


def check_username():
    """Ask for a username and grant or deny access."""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
                 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command',
                 'ExecState', 'InteractiveConsole', 'InterpreterInterface',
                 'StartServer', 'bob']
    username = input("Enter username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()
