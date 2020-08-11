list_1 = []
size = int(input("Enter the size of the list... "))
for i in range(size):
    list_1.append(int(input("Enter the element... ")))
splitting = int(input("To split the given list into equal number of sublists, enter the size of each sublist... "))
list_2 = [list_1[i : i + splitting] for i in range(0, size, splitting)]
print("The list afer splitting is\n",list_2)
