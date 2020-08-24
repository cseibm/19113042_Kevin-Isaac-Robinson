string = input("Enter a string with few characters replaced by '?'... ")
#creating empty string
new_string = ""
test = "pineapples"
#variable to start from the opposite end of the string
check = 1
for i in string:
    #? should be replaced with an appropriate lowercase alphabet
    if i == '?':
        
        #in the event that there is '?' in two corresponding positions, it can be replaced
        #with any letter. Here we use 'z'
        if string[-check] == '?':
            new_string += 'z' #'z' is appended to the new_string
            
        #if there is only 1 '?' in a corresponding position, it is replaced by
        #the corresponding alphabet in the string
        else:
            new_string += string[-check] #character in string[-check] is appended to new_string
    else:
        new_string += i #if i != '?', the new_string is appended with i
        
    check += 1 #check is incremented to continue traversal in reverse order
    
#printing output
if new_string == new_string[: : -1]:
    print("YES\nEntered string can be a palindrome if all '?' are replaced with necessary letters as follows... ", new_string)
else:
    print("NO") 
