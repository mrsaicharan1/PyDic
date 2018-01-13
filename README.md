# PyDic

A smart application which uses voice recognition technology to find out information about a certain word. 

# How to Run locally

* Install latest version of Python
* run `https://github.com/mrsaicharan1/PyDic.git` command in your terminal
* Enter into `project1` folder of cloned repository
* run `python -W ignore main.py` command 
* now you can query definition of words in the popped up CLI

# How it works

* User queries the definition of word in CLI
* word's meaning is displayed if it exist in database 
* otherwise it searches for the closest match of the queried word
* if closest match found by program is the required word, it prints word's meaning
* appropriate message is displayed if the required word doesn't exist in database

# Features :

* Smart exceptions which suggests few words if the CLI didn't understand your input
* JSON dataset containing dictionary of words and meanings

# Features being developed during OpenCode '18:
* Voice recognition capabilities
* GUI interfacing
* Explicit definitons and information about the word including sentence usage,antonyms,origin etc.


