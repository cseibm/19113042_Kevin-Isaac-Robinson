list = []
size = int(input("Enter the size of the list... "))
for i in range (size):
    list.append(input("Enter a string... "))
list_2 = [list[i] for i in range (size) if (list[i].count('e') >= 1 and list[i].count('t') >= 1)]
print(list_2)
