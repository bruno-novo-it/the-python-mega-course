import sys

def calculate_age(year):
    age = 2018 - year
    return age

user_age = calculate_age(int(sys.argv[1]))

print("You are {} years old".format(user_age))