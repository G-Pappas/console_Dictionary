"""
Simple Dictionary console application
"""

import json
from difflib import get_close_matches

data = json.load(open("data.json"))         #import of the dictionary

# function to check if word is in dictionary
def translate(word):
    word=word.lower()                       # conver word to lower letters, so program is not case sensitive
    if word in data:                        # if word is in dictionary it is printed
        return data[word]
    elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif word.upper() in data: #if user entered words like NATO (all capital)
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0: #check for similar words in case of user's false spelling,
                                                        # must be more than 0 because we want at least one row on our list
        user_answer= input("Did you mean %s instead? Enter Y if Yes, or N if No: " % get_close_matches(word,data.keys())[0])  #show the first element of the list
        if user_answer == "Y" or "y":                       #and ask user to say if it the one he wants
            return data[get_close_matches(word,data.keys())[0]]
        elif user_answer == "N" or "n":
            return "Sorry word doesn't exist."
        else :
            return "Sorry input error."
    else:
        return "Sorry word doesn't exist."



user_word = input("Enter word to get definition: ")          #get word from user
output = translate(user_word)
if type(output) == list: # Make print more user friendly, without commas and brackets if there are results
    for item in output:
        print(item)
else:
    print(output)

input("Press enter to exit")
