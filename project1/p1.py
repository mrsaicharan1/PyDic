import json
from difflib import get_close_matches
from PyDictionary import PyDictionary


data = json.load(open("data.json"))

#Function to display the initial message for the user
def display_initial_message():
    print "//////////////////////////////////////////////////////"
    print  "//   Welcome To PyDic, a python based dictionary.   //"
    print "//////////////////////////////////////////////////////"
    print "\n\n1. To search a word, just type in at the prompt.\n2. If the word is not found, similar words will be displayed.\n3. To quit, type in quit().\n4. To display this message again, type in message().\n"


def synonym(word):
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

def antonym(word):
	try:
		word = word.lower()
		dictionary = PyDictionary()
		anto_list = (dictionary.antonym(word))
		print("The antonym(s) of the word %s are:"%word)
		for i in range(0,len(anto_list)):
			print (str(i+1)+')'+anto_list[i].encode('ascii'))
	except TypeError:
		word = raw_input("Re-enter the word with the correct spelling: ")
		antonym(word)
	

if(__name__=='__main__'):
	display_initial_message()
	while True:
		word = raw_input("Enter word: ")
		if word == "quit()":
			quit()
		elif word == "message()":
			display_initial_message()
		else:
			choice = raw_input("Type A if you want to find the antonym or S if you want to find the synonym: ")
			if(choice=='A'):
				antonym = antonym(word)
			elif(choice=='S'):
				synonym = synonym(word)
				print synonym
