a = int(input("Enter the number of elements in the list...v"))
list = []
count = 0
for i in range(a):
    list.append(int(input("Enter the element: ")))
print ("The list is", list)
for j in list:
    if ((j % 2) != 0):
        count += 1
print ("The number of odd numbers is", count)
