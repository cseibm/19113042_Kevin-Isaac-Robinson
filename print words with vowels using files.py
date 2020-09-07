# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 16:59:56 2020

@author: Kevin Robinson
"""


write_file = open("Extract Vowels.txt", "w") #Creating 'Extract Vowels.txt' in write mode
#Writing data into created file
write_file.write("The words with vowels are to be extracted\nPineapples\nRhythm\nGrapes\nCrypt\nGreen\nGlyph\nBananas\nSky\nBall\nNymph\nDriad")
write_file.close() #Closing file

#Opening 'Extract Vowels.txt' in read mode
read_file = open("Extract Vowels.txt", "r")
#Creating new file to enter words in "Extract Vowels.txt' with vowels
vowel_file = open("Words with vowels.txt", "w")

list = read_file.read()
list = list.split() #To store the words in 'Extract vowels.txt' as  elements in the list

for i in list: 
    if 'a' in i or 'e' in i or 'i' in i or 'o' in i or 'u' in i: #checks if word contains lowercase vowel
        vowel_file.write(i) #writes the word in 'Words with vowels.txt'
        vowel_file.write("\n") #To add each word in new line
        """
        can use vowel_file.write(" ")
        to print all the words with vowels with space between each word
        """
    else:
        vowel_file.write("\n")
        
vowel_file.close() #Closing 'Words with vowels.txt' 
read_file.close() #CLosing 'Extract Vowles.txt'

print_file = open("Words with vowels.txt", "r") #Opening 'Words with vowels.txt' in read mode
print(print_file.read())       #printing 'Words with vowels.txt'
print_file.close() #closing 'Words with vowels.txt'
  
 
