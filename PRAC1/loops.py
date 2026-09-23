for i in range(1, 21, 2):
       print(i, end=' ')
print()

for i in range(0,100, 20):
       print(i, end=' ')



for i in range(20,0,-1):
    print(i, end=' ')



number_of_stars = input("input the number of stars: ")
for i in range(number_of_stars):
    print("*", end=' ')
print()


number_of_lines = int(input("input the number of lines: "))
for i in range(1, number_of_lines + 1):
    print("*" * i)