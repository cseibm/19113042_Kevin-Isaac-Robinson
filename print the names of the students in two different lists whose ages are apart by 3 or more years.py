import datetime
dict_1 = {}
dict_2 = {}
size = int(input("Enter the number of students in list 1... "))
for i in range(size):
    name = input("Enter the name of the student... ")
    year = int(input("Enter the year of birth of the student... "))
    month = int(input("Enter the month of birth of the student... "))
    date = int(input("Enter the day of birth of the student... "))
    DOB = datetime.date(year, month, date)
    dict_1[name] = DOB 
size = int(input("Enter the number of students in list 2... "))
for i in range(size):
    name = input("Enter the name of the student... ")
    year = int(input("Enter the year of birth of the student... "))
    month = int(input("Enter the month of birth of the student... "))
    date = int(input("Enter the day of birth of the student... "))
    DOB = datetime.date(year, month, date)
    dict_2[name] = DOB
today = datetime.date.today()
for i in dict_1:
    age_1 = today.year - dict_1[i].year - ((today.month, today.day) < (dict_1[i].month, dict_1[i].day))
    for j in dict_2:
        age_2 = today.year - dict_2[j].year - ((today.month, today.day) < (dict_2[j].month, dict_2[j].day))
        if age_1 - age_2 > 3:
            age_diff = age_1 - age_2
        if age_2 - age_1 > 3:
            age_diff = age_2 - age_1
        if age_diff > 3:
            print (i, "of list 1 and", j, "of list 2 have an age difference of", age_diff, "years")
    
