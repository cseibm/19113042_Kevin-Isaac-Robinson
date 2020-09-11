# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 12:07:47 2020

@author: Kevin Robinson
"""


write_file = open("Input File.txt", "w") #Creating 'Input File.txt' in write mode
#Writing data into created file
write_file.write("The line has 5 words\nwords in line2\nThis line has 7 words in it\nonly 3 words")
write_file.close() #Closing file

#Opening 'Input File.txt' in read mode
read_file = open("Input File.txt", "r")
#Creating new file '5 words lines.txt' to copy line in "Input File.txt' with 5 words or more 
copy_file = open("5 words lines.txt", "w")

list = read_file.read() #list now stores entire file 'Input File.txt'
list = list.split("\n") #To store the lines in 'Input File.txt' as  elements in a list

for i in list: 
    if i.count(" ") >= 4: 
        copy_file.write(i) #Copies the line with 5 or more words in '5 words lines.txt'
        copy_file.write("\n") #To add each line in new line
        """
        can use copy_file.write(" ")
        to print all the lines with 5 or more words with space between each line
        """
copy_file.close() #Closing '5 words line.txt' 
read_file.close() #CLosing 'Input File.txt'

print_file = open("5 words lines.txt", "r") #Opening '5 words lines.txt' in read mode
print(print_file.read())       #printing '5 words lines.txt'
print_file.close() #closing '5 words lines.txt'
