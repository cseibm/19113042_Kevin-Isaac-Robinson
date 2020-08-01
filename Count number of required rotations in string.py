str_1 = input("Enter a string... ")
str_2 = input("Enter a rotation of the same string... ")
copy = str_1
LR = 0
while (copy != str_2):
    L1 = str_1[0 : LR]
    L2 = str_1[LR :]
    copy = L2 + L1
    LR += 1
    if (LR > len(copy)):
        print("The second string cannot be acheived by rotating first string.\nPlease check inputs")
        exit(0)
copy = str_1
RR = 0
while (copy != str_2):
    R1 = str_1[0 : len(str_1) - RR]
    R2 = str_1[len(str_1) - RR :]
    copy = R2 + R1
    RR += 1
if(LR > 0 or RR > 0):
    LR -= 1
    RR -= 1
print(LR, "left-rotation(s) OR", RR, "right-rotation(s) were required to lead the first string to the second string")
