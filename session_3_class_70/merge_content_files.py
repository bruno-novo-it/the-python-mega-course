import glob2
from datetime import datetime

all_files = glob2.glob("*.txt")

all_files.sort()

print(all_files)

def merge_files(files, archive_name):
    with open(archive_name + ".txt","w") as myfile:
        for file in files:
            with open(file,"r") as content_file:
                #myfile.write(content_file.read() + "\n")
                content = content_file.readline()
                myfile.write("{}\n".format(content))


merge_files(all_files, datetime.now().strftime("%Y-%d-%m-%H-%M-%S-%s"))

# datetime.now().strftime("%Y-%d-%m-%H-%M-%S-%s")
# 2018-18-11-20-50-24-1542581424


#1. Consider using the glob2  third party library to generate a list of filenames 
#  to iterate through.

#2. Use a with  statement to create a new text file and then iterate through the 
# file list inside that with  statement and open and read existing file contents in 
# each iteration and write them to new text file.