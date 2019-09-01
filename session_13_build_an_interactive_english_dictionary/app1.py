import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data: #In cases User enter word like Paris or Delhi
        return data[w.title()]
    elif w.upper() in data: #In case User enter USA ou NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean {} intead? Y|y[Yes] N|n[No]:\n".format(get_close_matches(w,data.keys())[0]))
        if yn == "Y" or yn == "y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N" or yn == "n":
            return "The Word doesn't exist, Please double check it!!"
        else:
            return "You put an invalid Option!!"
    else:
        return "The Word doesn't exist, Please double check it!!"

word = input("Enter work: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)