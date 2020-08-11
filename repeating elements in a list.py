list_1 = []
size = int(input("Enter the size of the list... "))
for i in range(size):
    list_1.append(int(input("Enter the element... ")))
list_2 = [list_1[x] for x in range(size) if list_1.count(list_1[x]) > 1]
if list_2 == []:
    print("There are no repeating elements in the list")
else:
    print("The repeating elements are", list_2)
