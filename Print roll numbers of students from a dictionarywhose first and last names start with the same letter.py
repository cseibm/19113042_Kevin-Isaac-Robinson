student_dictionary = {}
roll_no_list = []
size = int(input("enter the number of students.... "))
for i in range(size):
    reg_no = int(input("Enter the reg_no... "))
    f_name = input("Enter the first name of the student... ")
    l_name = input("Enter the last name of the student... ")
    student_dictionary[reg_no] = [f_name, l_name]
temp = dict(student_dictionary)
for i in student_dictionary:
    name = student_dictionary[i]
    if name[0][0] == name[1][0]:
        roll_no_list.append(i)
if roll_no_list == []:
    print("There are no students whose first and last names start with the same letter")
else:    
    print("The roll numbers of the students whose first and last names start with the same letter are ", roll_no_list)
        
    
