a = int(input("Enter the number of elements in the list...v"))
list = []
count = 0
for i in range(a):
    list.append(int(input("Enter the element: ")))
print ("The list is", list)
sum = 0
for j in list[1::2]:
    sum += j
print("sum of odd index is", sum)
