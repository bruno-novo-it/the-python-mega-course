correct_password = "python123"

name = input("Enter name: ")

surname = input("Enter Surname: ")

password = input("Enter password: ")

while password != correct_password:
    password = input("\nThe password is Incorrect, try again: ")


message = "\nHi %s %s, you are logged in" % (name,surname)

print(message)