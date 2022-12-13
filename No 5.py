# // # //============================================================================
# // # // Name        : number2a.cpp
# // #  Author      : Jayd
# // # // Version     :
# // # // Copyright   : Your copyright notice
# // # // Description : Hello World in C++, Ansi-style
# // # //============================================================================


# /*
#  * Complete the 'pairs' function below.
#  *
#  * The function is expected to return an INTEGER.
#  * The function accepts following parameters:
#  *  1. INTEGER k
#  *  2. INTEGER_ARRAY arr
#  */



def countPairs(arr, n, k):
	count = 0

	for i in range(0, n):
		
		# Check for pair using the loop
		for j in range(i+1, n) :

			#int k: an integer, the target difference
			
            #int arr[n]: an array of integers
#using the condition if in the program to compare the arrars
			if arr[i] - arr[j] == k or arr[j] - arr[i] == k:count += 1
				
	return count

    #The given arrar
arr = [1, 2, 3, 4]

n = len(arr)

k = 1

#Printing the arrary that have the different target
print (f"Pair of the array {arr} that have a difference equal to the target value of {k} is ", countPairs(arr, n, k))