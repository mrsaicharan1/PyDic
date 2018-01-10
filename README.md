# PyDic

A python app which uses the CLI to query the definitions of a word in a dictionary.

# How to Run locally

* Install latest version of Python
* run `https://github.com/mrsaicharan1/PyDic.git`
* Enter into project1 folder of cloned repository
* run `python p1` (Linux users should make the script executable first)
* query definitions of words in the popped up interactive CLI

# How it works

* User queries the definition of words 
* if the word exists in database, it's meaning is print
* otherwise it searches for the close match of the queried word
* if close match is the required word, it prints it's meaning
* if the word doesn't exists in the database, it prints the appropriate message

# Features :

* Smart exceptions which suggests few words if the CLI didn't understand your input
* JSON dataset containing dictionary of words and meanings


