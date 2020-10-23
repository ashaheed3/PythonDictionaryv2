import json
import difflib

data = json.load(open("data.json"))
data = dict((k.lower(), v) for k, v in data.items())

word = ""

def define(word):
    word = word.lower()

    if word in data:
        return data[word]
    else:
        return "Sorry %s doesn't exit in the dictionary" %word

while word != "%": 
    word = input("Please enter a word: ")
    print(define(word))

   
  