# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 14:07:04 2020

@author: Kevin Robinson
"""

import sys

#dictionary that contains valid subjects and respective credits
credit_details_dict = {"SUBJECT1": 4, "SUBJECT2": 4, "SUBJECT3": 3, "SUBJECT4": 3, "SUBJECT5": 1, "SUBJECT6": 2, "SUBJECT7":2, "SUBJECT8": 8}
#dictionary containing the valid grades and corresponding GP
grade_dict = {"S": 10, "A": 9, "B": 8, "C": 7, "D": 6, "E": 5, "RA": 0, "AB": 0, "U": 0}
#list to store the subjects of the student
subject_list = []
#list to store the grades scored in each subject
grade_list = []
SGPA = 0
index = 0
total_credits = 0
number = int(input("Enter the amount of subjects.. "))

for i in range(number):
    #input the subject_list
    subject_list.append(input("Enter the subject... "))
    #input the grade_list
    grade_list.append(input("Enter the grade for the entered subject... "))
    
#Removing empty elements in list
count_sub = subject_list.count("") #counts empty elements in subject_list
count_grades = grade_list.count("") #counts empty elements in grade_list
for i in range(count_sub):
    subject_list.remove("") #removes first empty element from subject_list
for i in range(count_grades):
    grade_list.remove("") #removes first empty element from grade_list

#printing entered subject and grade lists
print("\n")
print("Subject_list = ", subject_list)
print("Grade_list = ", grade_list)

#in case of subject and grade mismatch
if len(subject_list) != len(grade_list):
    print("Subject list and Grade list Mismatch")
    sys.exit()

#Checking validity of inputs
for i in range(number):
    #checking for valid subjects
    if subject_list[i] not in credit_details_dict:
        print("Invalid Subjects")
        print("SGPA = 0.0")
        sys.exit()
    #checking for valid grades
    if grade_list[i] not in grade_dict:
        print("Invalid Grades")
        print("SGPA = 0.0")
        sys.exit()
        
#SGPA is case of RA/AB/U grades
if grade_list.count("RA") > 0 or grade_list.count("AB") > 0 or grade_list.count("U") > 0:
    print("SGPA = 0.0")
    sys.exit()
    
#calculate final answer in case of valid inputs
for i in subject_list:
    SGPA += credit_details_dict[i] * grade_dict[grade_list[index]]
    total_credits += credit_details_dict[i]
    index += 1 
SGPA = SGPA / total_credits
print("SGPA = ", round(SGPA,2))
