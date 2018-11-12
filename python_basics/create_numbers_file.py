numbers = [1, 2, 3]

number_file = open("number_file.txt", "W")

for number in numbers:
    number_file.write(str(number) + "\n")

number_file.close()