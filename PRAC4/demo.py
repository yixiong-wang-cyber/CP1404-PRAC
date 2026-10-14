def main():
    numbers = get_numbers()
    square_numbers(numbers)
    display_numbers(numbers)

def get_numbers():
    input_string = input("Enter numbers separated by commas: ")
    numbers_list = [float(num.strip()) for num in input_string.split(",")]
    return numbers_list


def square_numbers(numbers_list):
    for i in range(len(numbers_list)):
        numbers_list[i] = numbers_list[i] * numbers_list[i]



def display_numbers(numbers_list):
    numbers_list.sort()

    str_numbers = [str(num) for num in numbers_list]

    print("..".join(str_numbers))


if __name__ == '__main__':
    main()