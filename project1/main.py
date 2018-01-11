import json
import sys
from difflib import get_close_matches
from PyDictionary import PyDictionary
import pyttsx

data = json.load(open("data.json"))

#Function to display the initial message for the user
def display_initial_message():
    print "//////////////////////////////////////////////////////"
    print  "//   Welcome To PyDic, a python based dictionary.   //"
    print "//////////////////////////////////////////////////////"
    print "\n\n1. To search a word, just type in at the prompt.\n2. You can choose to view the Synonymns and the Antonymns of the word.\n3. To quit, type quit().\n4. To display this message again, type message().\n"

def textToSpeech(word):
	engine = pyttsx.init()
	engine.say(word)
	engine.runAndWait()

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
			antonym += [anto_list[i].encode('ascii')]
			print (str(i+1)+')'+anto_list[i].encode('ascii'))
			textToSpeech(antonym[i])
	except TypeError:
		print("Please re enter the world below with the right spelling! ")


def antonym(word):
	try:
		word = word.lower()
		dictionary = PyDictionary()
		anto_list = (dictionary.antonym(word))
		print("The antonym(s) of the word %s are:"%word)
		textToSpeech("The antonyms of the word you entered are")
		antonym=[]
		for i in range(0,len(anto_list)):
			antonym += [anto_list[i].encode('ascii')]
			print (str(i+1)+')'+anto_list[i].encode('ascii'))
			textToSpeech(antonym[i])
	
	except TypeError:
		print("Please re enter the world below with the right spelling! ")


if(__name__=='__main__'):
	display_initial_message()
	while True:
		word = raw_input("\nEnter word: ")
		if word == "quit()":
			quit()
		elif word == "message()":
			display_initial_message()
		else:
			choice = raw_input("\nType\n\tA : find antonym\n\tS : find the synonym\n\tQ : Quit\n\tChoice = ")
			if(choice=='A' or choice=='a'):
				antonym = antonym(word)
			elif(choice=='S' or choice=='s'):
				synonym = synonym(word)
				print("The synonym(s) of the word %s are:"%word)
				textToSpeech("The synonyms of the word that you entered are")
				for i in range (0,len(synonym)):
					synonym[i]=synonym[i].encode('ascii')
					print (str(i+1)+')'+synonym[i])
					textToSpeech(synonym[i])
			elif(choice=='Q' or choice=='q'):
				sys.exit()
