"""Convert Fahrenheit temperatures from a file to Celsius and write them out."""


def main():
    """Read Fahrenheit temps from temps_input.txt and write Celsius to temps_output.txt."""
    with open("temps_input.txt", "r") as in_file, open("temps_output.txt", "w") as out_file:
        for line in in_file:
            fahrenheit = float(line)
            celsius = fahrenheit_to_celsius(fahrenheit)
            out_file.write(f"{celsius}\n")


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return 5 / 9 * (fahrenheit - 32)


main()
