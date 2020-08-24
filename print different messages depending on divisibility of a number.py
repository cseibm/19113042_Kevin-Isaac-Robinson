def Solution (number):
    for i in range(1, number + 1):
        if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
            print ("CodilityTestCoder")
            continue #continue is used to skip the statements in the current iteration and move to the next
            
        if i % 2 == 0 and i % 3 == 0:
            print ("CodilityTest")
            continue
        
        if i % 2 == 0 and i % 5 == 0:
            print ("CodilityCoder")
            continue
        
        if i % 3 == 0 and i % 5 == 0:
            print ("TestCoder")
            continue
        
        if i % 2 == 0:
            print ("Codility")
            continue
        
        if i % 3 == 0:
            print ("Test")
            continue
            
        if i % 5 == 0:
            print ("Coder")
            continue
        
        print(i)   
    
    
input_number = int(input("Enter a number... "))
Solution (input_number)
