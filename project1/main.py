import json
import os
import sys
from difflib import get_close_matches
from PyDictionary import PyDictionary
from Tkinter import *
from bs4 import BeautifulSoup
import requests

dictionary = PyDictionary()


data = json.load(open("word_reference.json"))



def getSoup(url):
	response = requests.get(url)				#sending request
	response = response.text				#getting text from request
	return BeautifulSoup(response,'html.parser')

def wordOfTheDay():
    entry.delete(0, END)
    soup = getSoup("https://en.oxforddictionaries.com/explore/word-of-the-day")		
    wotd = soup.find('a',attrs={'class':'linkword'})	
    wotd = wotd.text
    url = "https://en.oxforddictionaries.com/definition/" + wotd
    soup = getSoup(url)
    adj = soup.find('span',attrs={'class':'ind'})
    origin = soup.find('div',attrs={'class':'senseInnerWrapper'})
    pronounciation = soup.find('span',attrs={'class':'phoneticspelling'})
    exampleSentence = soup.find('li',attrs={'class':'ex'})
    synonyms = soup.find('div',attrs={'class':'exs'})
    wotd_info = {"Synonyms:" : synonyms,"Origin:" : origin, "Adjective:" : adj, "Pronunciation:" : pronounciation, "Example Sentence:" : exampleSentence}
    k = 1


    global frame_2
    frame_2.destroy()
    frame_2 = Frame(root)
    frame_2.pack(side = BOTTOM)
    label = Label(frame_2, text = "", width = 150)
    label.grid(row = 4)
    label = Label(frame_2, text = "Word Of The Day:", width = 150)
    label.grid(row = 4)
    label = Label(frame_2, text = wotd, width = 150)
    label.grid(row = 5)
    

    for i,j in wotd_info.items():
        label = Label(frame_2, text = " ", width = 150)
        label.grid(row = 5 + k)
        label = Label(frame_2, text = i, width = 150)
        label.grid(row = 6 + k)
        try:
            label = Label(frame_2, text = j.text, width = 150)
            label.grid(row = 7 + k)
        except:
            label = Label(frame_2, text = i[:len(i)-1] + ' not found', width = 150)
            label.grid(row = 7 + k)
        k += 3
    



def textToSpeech(word):
	command = "espeak "
	command += "\'"+word+"\'"
	os.system(command)


        
#Calls the meaning() function
def loop_meaning():

    #Create Frame
    global frame_2
    frame_2.destroy()
    frame_2 = Frame(root)
    frame_2.pack(side = BOTTOM)
    label = Label(frame_2, text = "", width = 150)
    label.grid(row = 4)

    #Input Word
    word = entry.get()
    meaning(word,label)

#Calls the synonym function
def loop_synonym():

    #Create Frame
    global frame_2
    frame_2.destroy()
    frame_2 = Frame(root)
    frame_2.pack(side = BOTTOM)
    label = Label(frame_2, text = "", width = 150)
    label.grid(row = 4)

    #Input Word
    word = entry.get()
    synonym(word,label)


#Calls the antonym function
def loop_antonym():

    #Create Frame
    global frame_2
    frame_2.destroy()
    frame_2 = Frame(root)
    frame_2.pack(side = BOTTOM)
    label = Label(frame_2, text = "", width = 150)
    label.grid(row = 4)

    #Input Word
    word = entry.get()
    antonym(word,label)



#Function to get the meaning
def meaning(word,label):

    try:
        word = word.lower()
        matches=get_close_matches(word,data.keys())
        if matches[0] != word:
            word = matches[0]
        entry.delete(0, END)
        entry.insert(0,word)
        mean_dict = (dictionary.meaning(word))
        label = Label(frame_2, text = "Meaning:", width = 150)
        label.grid(row = 4)

        j = 1;
        if mean_dict["Noun"]:
            Label(frame_2, text= "Noun:" , width = 100).grid(row = 5)
            for i in mean_dict["Noun"]:
                Label(frame_2, text= str(j) + ". " +i , width = 100).grid(row = 6 + j -1)
                textToSpeech(i)
                j += 1
        if mean_dict["Verb"]:
            Label(frame_2, text= "Verb:" , width = 100).grid(row = 6 + j - 1)
            for k in mean_dict["Verb"]:
                Label(frame_2, text= str(j) + ". " +k , width = 100).grid(row = 7 + j -1)
                textToSpeech(k)
                j += 1

    except TypeError:
        Label(frame_2, text= "Meaning not found").grid(row = 4)
        textToSpeech("Meaning not found")



#Function to get the synonyms
def synonym(word,label):
    try:
        word = word.lower()
        matches=get_close_matches(word,data.keys())
        if matches[0] != word:
            word = matches[0]
        entry.delete(0, END)
        entry.insert(0,word)
        syno_list = (dictionary.synonym(word))
        label = Label(frame_2, text = "Synonyms:", width = 150)
        label.grid(row = 4)
        for i in range(0,len(syno_list)):
            Label(frame_2, text= (str(i+1)+')'+syno_list[i]), width = 100).grid(row = 5 + i)
            textToSpeech(syno_list[i])

    except TypeError:
        Label(frame_2, text= "Synonym not found").grid(row = 4)
        textToSpeech("Synonym not found")


#Function to get the antonyms
def antonym(word,label):
    try:
        word = word.lower()
        matches=get_close_matches(word,data.keys())
        if matches[0] != word:
            word = matches[0]
        entry.delete(0, END)
        entry.insert(0,word)
        anto_list = (dictionary.antonym(word))
        label = Label(frame_2, text = "Antonyms:", width = 150)
        label.grid(row = 4)
        for i in range(0,len(anto_list)):
            Label(frame_2, text= (str(i+1)+')'+anto_list[i]), width = 100).grid(row = 5 + i)
            textToSpeech(anto_list[i])

    except TypeError:
        Label(frame_2, text= "Antonym not found").grid(row = 4)
        textToSpeech("Antonym not found")
	
#Initialize root canvas
root = Tk()
root.title("PyDic")


if(__name__=='__main__'):

	#Create Frames
    frame_1 = Frame(root)
    frame_1.pack()
    frame_2 = Frame(root)
    frame_2.pack(side = BOTTOM)

    #Input Word
    message = Label(frame_1, text = "Enter word", width = 150)
    message.grid(row = 0) 
    entry = Entry(frame_1)
    entry.grid(row = 1)

    #Display Buttons
    btn = Button(frame_1, text  = "Search Meaning", command = loop_meaning)
    btn.grid(row = 3)
    btn = Button(frame_1, text  = "Search Synonym", command = loop_synonym)
    btn.grid(row = 4)
    btn = Button(frame_1, text  = "Search Antonym", command = loop_antonym)
    btn.grid(row = 5)
    btn = Button(frame_1, text  = "Word of the Day", command = wordOfTheDay)
    btn.grid(row = 6)
	
    root.mainloop()
				



