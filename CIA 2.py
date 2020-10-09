def if_even(list):
    sum = 0
    for i in list:
        sum = 0
        i = str(i)
        for j in i:
            sum = sum+int(j)
        if(sum%2 == 0):
            print("element with even sum of digits is...", i)
        
def if_odd(list):
    sum = 0
    for i in list:
        sum = 0
        i = str(i)
        for j in i:
            sum = sum+int(j)
        if(sum%2 != 0):
            print("element with odd sum of digits is...", i)

l = []        
n = int(input("Enter the number of elements n the list... "))
for i in range(n):
    l.append(int(input("Enter the element... ")))
if_even(l)
n = int(input("to find elements whose sum of digits is odd, enter 1... "))
if n == 1:
    if_odd(l)
else:
    print("INVALID INPUT")
