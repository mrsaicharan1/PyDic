import json

import sys

from difflib import get_close_matches

from PyDictionary import PyDictionary




dictionary=PyDictionary()

    

#Function to display the initial message for the user

def display_initial_message():

    print "//////////////////////////////////////////////////////"

    print  "//   Welcome To PyDic, a python based dictionary.   //"

    print "//////////////////////////////////////////////////////"

    print "\n\n1. To search a word, just type in at the prompt.\n2. You can choose to view the Synonymns and the Antonymns of the word.\n3. To quit, type quit().\n4. To display this message again, type message().\n"









def antonym(word):

	try:

		word = word.lower()

		dictionary = PyDictionary()

		anto_list = (dictionary.antonym(word))

		print("The antonym(s) of the word %s are:"%word)

		for i in range(0,len(anto_list)):

			print (str(i+1)+')'+anto_list[i].encode('ascii'))
			return 'These are the antonyms'

	except TypeError:

		word = raw_input("Re-enter the word with the correct spelling: ")

		antonym(word)

	



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

				antonym = dictionary.antonym(word)
				print antonym

			elif(choice=='S' or choice=='s'):

				synonym = dictionary.meaning(word)
				print synonym 
			
			elif(choice=='Q' or choice=='q'):

				sys.exit()