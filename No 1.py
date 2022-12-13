# //============================================================================
# // Name        : number2a.cpp
#  Author      : Jayd
# // Version     :
# // Copyright   : Your copyright notice
# // Description : Hello World in C++, Ansi-style
# //============================================================================


#Function to compare
def comp(c, d):
    #A as alice 
    A = 0
    #B as Bob
    B = 0
    #Opening for loop
    for i in range(len(c)):
#Condition if to compare
        if c[i] > d[i]:
            A += 1
            #If the firt statement is not working then second
        elif c[i] < d[i]:
            #Incremantation 
            B += 1
    return A, B

#Finally we print 
print(comp([6, 7, 2], [19, 5, 4]))


#                           PSDEUDO

# Define function with alice and bob points as parameter=1
# Initialize alice ponts to zero=1
# Initialize bob points to zero=1
# For loop for looping around bob’s and alice’s points=n
# If statement to check if in alice’s array,a[i] is greater than b[i] in bob’s array=1
# Alice will get point=1
# If  a[i] in alice’s array is less than b[i] in bob’s array=1
# Bob will get point=1
# Return alice and bob points=1
# call function to print alice and bob ponts=1