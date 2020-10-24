import json
from difflib import get_close_matches

data = json.load(open("data.json"))
data = dict((k.lower(), v) for k, v in data.items())

word = ""

def define(word):

    word = input("Please enter a word: ")
    word = word.lower()

    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        replace = input("Sorry %s doesn't exist in the dictionary. Did you mean %s instead? [Y/N] " % (word, get_close_matches(word, data.keys())[0]))
              
        if replace.upper() == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return "Sorry %s doesn't exit in the dictionary. Please check your input" %word
    else:
        return "Sorry %s doesn't exit in the dictionary" %word

while word != "%":
    result = define(word)

    if type(result) == list:
        for item in output:
            print(item)
    else:
        print(result)

   
  