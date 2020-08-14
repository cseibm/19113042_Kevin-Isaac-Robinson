student_dictionary = {}
name_list = []
size = int(input("enter the number of students.... "))
for i in range(size):
    reg_no = int(input("Enter the reg_no... "))
    name = input("Enter the name of the student... ")
    age = int(input("Enter the age of the student... "))
    student_dictionary[reg_no] = [name, age]
temp = dict(student_dictionary)
for i in student_dictionary:
    student = student_dictionary[i]
    if student[1] > 18:
        name_list.append(student[0]) 
        temp.pop(i)
if name_list == []:
    print("There are no students who are older than 18")
else:    
    print("The students who are older than 18 are ", name_list)
    print("The dictionary whithout those over 18 is\n", temp)
        
    
