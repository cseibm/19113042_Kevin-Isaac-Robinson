def no_of_odd(sub, list_odd): #funtion to count the number of odd nos in a subist
    count = 0
    for i in sub:
        if i % 2 != 0:
            count += 1
    list_odd.append(count) #Entering the number of odd numbers in each sublist into a seperate list
    
def no_of_even(sub, list_even): #funtion to count the number of even nos in a subist
    count = 0
    for i in sub:
        if i % 2 == 0:
            count += 1
    list_even.append(count) #Entering the number of even numbers in each sublist into a seperate list
    
def max_sum(sub, list_max): #funtion to find the sum of elements in a subist
    sum = 0
    for i in sub:
        sum += i
    list_max.append(sum) #Entering the sum of elements in each sublist into a seperate list
    
        

main_list = []
odd_list = []
even_list = []
max_list = []
size = int(input("Enter the number of sublist... "))
temp = size
for i in range (size): #iterates once for each sublist
    sub_list = []
    size = int(input("Enter the size sublist... ")) #iterates for size of sublist times
    for j in range (size):
        sub_list.append(int(input("Enter the element in the sublist... "))) #adding elements to a sublist
    main_list.append(sub_list) #appending sublists to form a main list
for i in range (temp): #the user defined functions must be called once each for every sublist in the main list
    no_of_odd(main_list[i], odd_list)
    no_of_even(main_list[i], even_list)
    max_sum(main_list[i], max_list)
print("The entered list is\n\t", main_list,"\n")

"""
next 3 lines are used to find the index of lists that
satisfy the given conditions
"""

most_odd = odd_list.index(max(odd_list))
most_even = even_list.index(max(even_list))
maximum = max_list.index(max(max_list))

print ("The sublist with the most number of odd numbers is sublist ", most_odd+1) #since index starts from zero, the number of the list is + 1 
print ("The sublist with the most number of even numbers is sublist ", most_even+1)
print ("The sublist with the max sum of elements is sublist ", maximum+1)
