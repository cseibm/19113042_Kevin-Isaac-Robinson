a = int(input("Enter the first number\t"))
b = int(input("Enter the second number\t"))
i=1
while (i <= a and i<= b):
    if (a % i == 0 and b % i == 0):
        gcf=i
    i+=1
a = int(a / gcf)
b = int(b / gcf)
print("Ratio of the two entered numbers is\n", a, ":", b)
