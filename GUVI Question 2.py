list = input()
sum = 0
length = 0
MyKey = {}
HitsKey = {}
multiply = 2
for i in list:
    string = str(i)
    sum = 0
    for j in string[0: : 2]:
        sum += int(j)
    while sum in MyKey:
        sum *= multiply
        multiply += 1
    MyKey[sum] = i
    sum = 0
    multiply = 2
    for j in string[1: :2]:
        sum += int(j)
    while sum in HitsKey:
        sum *= multiply
        multiply += 1
    HitsKey[sum] = i
print(MyKey)
print(HitsKey)
