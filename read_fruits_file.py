
fruits_file = open("fruits.txt", "r")

fruit_content = fruits_file.read() # CAN USE read() OR readlines() to read a file
# fruit_content = file.readlines()
# fruit_content = [line.strip() for line in fruit_content]

fruits_file.close()

#print(fruit_content)

## THIS WILL PRINT EACH CARACTER IN ONE LINE
# for c in fruit_content:
#     print(c)

## THIS WILL CONVERT ALL THE WORDS TO A LIST AND PRINT THEM
fruit_content = fruit_content.splitlines()
for i in fruit_content:
    print(i)

print("\n\n")

##THIS WILL PRINT THE LENGHT OF FRUITS NAMES
for fruit in fruit_content:
    print(len(fruit))
