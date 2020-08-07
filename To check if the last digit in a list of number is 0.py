def check_list(list):
    list_2 = []
    for i in list:
        if(i % 10 == 0):
            list_2.append(i)
    print ("The elements in the entered list with 0 as the last digit are", list_2)
        
a = int(input("Enter the number of elements in the list... "))
list_1 = []
check = 0
for i in range(a):
    list_1.append(int(input("Enter the element: ")))
check_list(list_1)
