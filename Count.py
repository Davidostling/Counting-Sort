A = [2, 2, 1, 2, 5, 2, 3, 1] #input array
Count=[] #corresponding count array to above input

sortedA = []
for i in range(0, max(A)+1): #initializes Count with 0:s
    Count.append(0)
for j in range(0, len(A)):
    Count[A[j]]+=1 #Counts all elements
print("Count: ", Count)
for i in range(0, len(Count)):
    for j in range(Count[i]): 
        sortedA.append(i) #Returns copies of all elements
print("Sorted: ", sortedA)
