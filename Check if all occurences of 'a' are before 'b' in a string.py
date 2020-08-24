def Solution(temp, a_c, b_c):
    #if there are 0 'a's or 'b's the output is TRUE
    if a_c == 0 or b_c == 0:
        print("TRUE")
        sys.exit()
    #duplicate value of b_count for comparison
    b_temp = b_c
    
    for i in range(len(temp)):
        #starting from index zero, 1 is subtracted from the respective counts with every occurence
        if temp[i] == 'a':
            a_c -= 1
        else:
            b_temp -= 1
            
        #if the count 'a' gets is reduced to 0 while the count of 'b' remains unchaged
        #all occurences of 'a' are before 'b' and hence the output is true    
        if a_c == 0 and b_temp == b_c:
            print("TRUE")
            sys.exit()
            
        #if the count of 'b' is reduced before the count of 'a' reaches 0
        #All occurences of 'a' are not before 'b' and hence the output is false    
        if b_temp < b_c and a_c > 0:
            print("FALSE")
            sys.exit()
    


import sys
string = input()
#To exit code if any characters other than 'a' or 'b' are present in the string
for i in string:
    if i == 'a' or i =='b':
        continue
    else:
        print("FAIL")
        sys.exit()
#to find the number of occurences of 'a' and 'b' in the input string
a_count = string.count('a')
b_count = string.count('b')
Solution(string, a_count, b_count)
