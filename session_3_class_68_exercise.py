# Ugly way to make the interaction

# temperatures = [10, -20, -289, 100]
# def c_to_f(c):
#     if c < -273.15:
#         return "That temperature doesn't make sense!"
#     else:
#         f = c* 9/5 + 32
#         with open("session_3_class_68_exercise_temperatures.txt", "a+") as temperatures_result:
#             temperatures_result.write("{}\n".format(f))

# for t in temperatures:
#     c_to_f(t)


# Better Solution, treat temperature input and
# file path as arguments, less code and better
# identation

temperatures = [10, -20, -289, 100]

def writer(temperature, file_path):
    with open(file_path, "w") as file:
        for c in temperature:
            if c > -273.15:
                f = c* 9/5 + 32
                file.write("{}\n".format(f))

writer(temperatures, "session_3_class_68_exercise_temperatures.txt")