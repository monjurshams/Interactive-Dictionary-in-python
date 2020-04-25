# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 18:26:57 2020

@author: Monjur Bin Shams
"""
import json
from difflib import get_close_matches

#saving the dictionary in a variable format from json format
dict = json.load(open("dict.json",'r'))         


#function for searching the word in the dictionary
def searchword(word):                           
    word = word.lower()
    if word in dict:
        return dict[word]
    
#get_close_match returns a list of close matches. So we check if the length of that list is greater than zero
#if it is greater than zero, then we give the first index to the user to check
    elif len(get_close_matches(word, dict.keys()))>0:           
        c2 = input("Did you mean %s? y/n: " %get_close_matches(word, dict.keys())[0]) 
        c2.lower()
        if (c2 == "y"):
            return dict[get_close_matches(word, dict.keys())[0]]
        elif c2=="n":
            return "\nThe word does not exist in the dictionary"
        else:
            return "\nInvalid choice, better luck next time"
    else:
        return "\nThe word does not exist in the dictionary"

#function for choosing to search again without closing the program
def choice(c):
    if (c=='y'):
       word = input("Enter the word:")
       inputword(word)
    elif c=="n":
        print("\nThanks for using the dictionary")
        return
    else:
        print("\nInvalid choice, better luck next time")
        return 

#function for processing the input word and taking the choice for searching again
def inputword(word):    
        output = ((searchword(word)))
        if type(output)==list:
            for item in output:
                print(item)
        else:
            print(output)
        c = input("\nDo you want to search again? If yes, press y/n:")
        c.lower()
        choice(c)

#taking input from the user
word = input("Enter the word:")
inputword(word)


