# //============================================================================
# // Name        : number2a.cpp
#  Author      : Jayd
# // Version     :
# // Copyright   : Your copyright notice
# // Description : Hello World in C++, Ansi-style
# //============================================================================

# Definning the functuon MAXGF
def maxgf(prices, k):
    #Initializing the sorted prices 
    sortedPrices = sorted(prices)
    
    #Initializing the total to 0
    total = 0
    #Function Arrary
    gf = []

    #For loop
    for i in range(len(sortedPrices)):
        #Condition If 
        if total + sortedPrices[i] <= k:
            total += sortedPrices[i]
            gf.append(sortedPrices[i])
        else:
            break
    print(f"Mark can buy  {gf} toys for a total of {total}")
    print(f"The maximum toy of {k} is {len(gf)} ")


prices = [2, 3, 1, 6, 4, 7]
k = 12
print(maxgf(prices, k))
              

                                    
#                           PSDEUDO

# Define the function maxgf
# Initializing the sorted price 
# Initializing the total to 0
# Open the arrary gf
# Using the for loop 
# Using the if condition
# Breaking if the condition is not true
# orinting the gf and total price
# Price equeal the given array
# initializing K aialble 
# Then print the price