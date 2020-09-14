NK = input() #first line input
NK = NK.split()
a = input() # second line input
a = a.split() #input to list
#N = int(NK[0]) 
K = int(NK[1])
list = []
sum = 0
for i in a:
    list = []
    for j in range(int(i) -int(K), int(i) + (int(K)+1)):
        list.append(j) #making list for each element in a with range(i-K, i+k)
        
    for k in list:
        if str(k) != i and str(k) in a: #checking if element in list is present in input
            sum+=1
            break
print (sum)
