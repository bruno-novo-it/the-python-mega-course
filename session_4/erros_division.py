def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Zero division is Meaningless"

print(divide(1,1))

print("End of program")