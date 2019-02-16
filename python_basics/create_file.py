myfile = open("employees.txt", "w")

#myfile = open("employees.txt", "a") --> Option a is to append something to an
                                        # existing file BUT NOT READ IT

#myfile = open("employees.txt", "a+") --> Option a is to append something to an
                                        # existing file and READ IT to

myfile.write("Mike")

myfile.write("\nJack")

myfile.write("\nJoe")

myfile.close()