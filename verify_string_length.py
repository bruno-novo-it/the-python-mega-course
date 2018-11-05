import sys

# If we don't use the input function(always give string) and we
# need to avoid Int value Types

def string_length(mystring):
    if type(mystring) == int:
        return "Sorry, integers don't have length"
    elif type(mystring) == float:
        return "Sorry, float types don't have length"
    else:
         return len(mystring)

# def string_length(mystring):
#     return len(mystring)

user_input = input("\nDigite uma palavra: ")

print("\nA palavra contém {} letras!\n".format(string_length(user_input)))