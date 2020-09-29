# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 15:54:32 2020

@author: Kevin Robinson
"""


class list:
    ages = []
    
    def __init__(self, a):
        self.ages = a
        
    def display(self):
        print("Object with more than 2 ages is ", self, "\n")
        
    def check(self):
        if len(self.ages) > 2:
            return True
            
n = int(input("Enter the number of objects... "))
obj_list = []
for i in range (n):
    age_list = []
    print("Enter the ages for object ", i+1, "... ")
    age_list= input()
    age_list = age_list.split()
    obj_list = list(age_list)
    if obj_list.check() == True:
        obj_list.display()
    else:
        print("No. of ages < 2\n")
    
    
