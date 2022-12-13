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

# Define function with A and B points as parameter=1
# Initialize A ponts to zero=1
# Initialize B points to zero=1
# For loop for looping around B’s and alice’s points=n
# If statement to check if in alice’s array,a[i] is greater than b[i] in B’s array=1
# A will get point=1
# If  a[i] in alice’s array is less than b[i] in B’s array=1
# B will get point=1
# Return A and B points=1
# call function to print A and B ponts=1