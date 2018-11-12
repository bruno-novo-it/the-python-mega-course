
mylist = [1, 2, 3, 4, 5]

for item in mylist:
    print(item)

#THIS WILL PRINT:
# 1
# 2
# 3
# 4
# 5


print("\n\n")

a = "Tricky"

for i in a[:3]:
    print(i)

#THIS WILL PRINT:
# T
# r
# i

print("\n\n")

mylist = ["Trickier"]

for item in mylist:
    print(item)

#THIS WILL PRINT:
# Trickier --> THERE IS ONLY ONE ELEMENT INSIDE THE LIST

print("\n\n")

mylist = ["Trickier"]

for item in mylist[0]:
    print(item)

#THIS WILL PRINT:
# T
# r
# i
# c
# k
# i
# e
# r
# WE ARE INTERATING THE ELEMENT INSIDE THE LIST, THE FIRST AND ONLY ELEMENT

print("\n\n")

mylist = ["Terribly Tricky"] 

for word in mylist:
    for letter in word[-6:]:
        print(letter)

#THIS WILL PRINT:
# T
# r
# i
# c
# k
# y

print("\n\n")

list_2_46 = [1, 2, 3, 4, 5]

for item in list_2_46:
    if item > 2:
        print(item)