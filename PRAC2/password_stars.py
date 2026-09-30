"""Password check program that prints asterisks for each password character."""

MIN_LENGTH = 8


def main():
    """Get a valid password and print asterisks matching its length."""
    password = get_password()
    print_asterisks(password)


def get_password():
    """Get a password that meets the minimum length requirement."""
    password = input(f"Enter a password (minimum {MIN_LENGTH} characters): ")
    while len(password) < MIN_LENGTH:
        print(f"Password must be at least {MIN_LENGTH} characters long.")
        password = input(f"Enter a password (minimum {MIN_LENGTH} characters): ")
    return password


def print_asterisks(password):
    """Print as many asterisks as the length of password."""
    print("*" * len(password))


main()
