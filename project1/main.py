import json

import sys

from difflib import get_close_matches

from PyDictionary import PyDictionary

import os


dictionary=PyDictionary()

    

#Function to display the initial message for the user

def display_initial_message():

    print "//////////////////////////////////////////////////////"

    print  "//   Welcome To PyDic, a python based dictionary.   //"

    print "//////////////////////////////////////////////////////"

    print "\n\n1. To search a word, just type in at the prompt.\n2. You can choose to view the Synonymns and the Antonymns of the word.\n3. To quit, type quit().\n4. To display this message again, type message().\n"




def textToSpeech(word):
	command = "espeak "
	command += "\'"+word+"\'"
	os.system(command)




def antonym(word):

	try:

		word = word.lower()

		dictionary = PyDictionary()

		anto_list = (dictionary.antonym(word))

		print("The antonym(s) of the word %s are:"%word)

		textToSpeech("The antonyms of the word that you entered are:")

		antonym = []

		for i in range(0,len(anto_list)):
			antonym += [anto_list[i].encode('ascii')]
			print (str(i+1)+')'+anto_list[i].encode('ascii'))
			textToSpeech(antonym[i])

	except TypeError:

		word_new = raw_input("Re-enter the word with the correct spelling: ")

		antonym(word_new)

	



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
				#print antonym

			elif(choice=='S' or choice=='s'):

				synonym = dictionary.meaning(word)
				
				synonym_list = synonym.values()
				
				synonym_list = synonym_list[0]
				
				print ("The synonym(s) of the word %s are:\n"%word)
				
				textToSpeech("The synonyms of the word that you entered are")
				
				for i in range(0,len(synonym_list)):
					
					print (str(i+1)+')'+synonym_list[i])
					
					textToSpeech(synonym_list[i])
			
			elif(choice=='Q' or choice=='q'):

				sys.exit()
