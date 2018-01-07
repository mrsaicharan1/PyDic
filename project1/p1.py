import json
from difflib import get_close_matches
data = json.load(open("data.json"))
def translate(word):
    word = word.lower()
    lnth = len(get_close_matches(word, data.keys()))
    matches=get_close_matches(word,data.keys())
    if word in data:

        return data[word]

    elif lnth > 0:
        print("Did you mean %s?"%get_close_matches(word,data.keys())[0])
        word = raw_input("Enter yes/no: ")
        if(word=='yes'):
            print(translate(word))
        elif(word=='no'):
            word = raw_input("Enter word: ")
            print(translate(word))

    else:
        return 'Please check the spelling'
word = raw_input("Enter word: ")
print(translate(word))


