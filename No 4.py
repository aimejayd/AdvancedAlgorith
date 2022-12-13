
# //============================================================================
# // Name        : number2a.cpp
#  Author      : Jayd
# // Version     :
# // Copyright   : Your copyright notice
# // Description : Hello World in C++, Ansi-style
# //============================================================================

#Defining the function
def lilysHomework(arr):

    #Return the minimum swaps in asc older and desc in the arrary
    return min(minSwapsAsc(arr), minSwapsDesc(arr))
 
 #Define the function to swaps the minimum desc


def minSwapsDesc(arr):
    positions = [ n = len(arr)
    visited = [False for _ in range(n)]
    ans = 0

    #Opening the for loop in the range of n
    for i in range(n):

        #If condintion being used 
        if visited[i] or positions[i] == i:
            # Continue to the other cycle
            continue
       
        cycle_size = 0
        j = i

        #Using the while loop when its not visited
        while not visited[j]:
            visited[j] = True
            j = positions[j]
            cycle_size += 1
       #If condition of the cycle size
        if cycle_size > 0:
            ans += (cycle_size - 1)x[0] for x in sorted(enumerate(arr), key=lambda x: x[1], reverse=True)]