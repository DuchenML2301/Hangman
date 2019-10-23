import turtle
import time
import os
import random
misses = []
misses = 0
hangmanList = [''' 
 
     +---+
     0   |
         |
         |
         === ''', '''
      +---+
      0   |
      |   |
          |
          === ''', '''
      +---+
      0   |
      |   |
       \  |
          === ''', '''
      +---+ 
      0   |
      |   |
     / \  |
           === ''', '''
      +---+ 
      0   |
      |\  |
     / \  |
         === ''', '''
      +---+
      0   |
     /|\  |
     / \  |
         === ''' ]
         
misses = 0

while misses < 7:
	guess = input("Guess a letter: ")
	if guess in secretWord:
		#looop through secret word and change my guesss list at the correct lndexs
		print("letter is in the word")
	else:
		misses += 1
		print(hangmanList[misses])
print("GAME OVER")

def main(t):
	alphabet = ["a","b","c", "d", "e", "f", "g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
wordlist= "ponyo"
wordlist = list(secretWord)
  
#missNum = input("How many misses would it take to lose??: ")


choice = input("Type a letter: ")

myString = (wordlist[0])
myList = list(myString)
print(myList)

GuessList = []
for a in myList:
	GuessList.append("_")

print(GuessList)

GuessList[2] = [choice]
print(GuessList)


if choice == myString:
	print("Its a match")
	
else:
	print("Not a match")
# how to check if a letter is in a word
letter = input("Type a lette: ")
if letter in myString:
	print("Letter is in the word!")
	print(GuessList)

else:
	print("letter is NOT in the word")
	print(GuessList)

count = 0
for l in myString:
	if l == letter:
		print(count)
	count += 1
