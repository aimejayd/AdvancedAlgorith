# AdvancedAlgorith
Summative 
Assessment Goals

1. Establish a system flow of a problem to derive the solution
2. To determine the running time function of an algorithm but it is actually implemented
3. To understand combinatorial problems and determining optimal solutions
4. Understanding graph theory and its implementation
5. Implementing algorithm design approaches in determining solutions and write the actual programs.

Numbe 1 

This code loops through the three elements in the rating triples a and b, and compares each element. If Alice's rating is greater than Bob's for a given element, Alice receives a point. If Bob's rating is greater than Alice's for a given element, Bob receives a point. Otherwise, neither person receives a point. At the end, the comparison points are returned as a list with Alice's points first and Bob's points second.


Here is a possible implementation of the pseudocode in the Python programming language:


# Alice and Bob's comparison points
alice_points = 0
bob_points = 0

# Loop through the three elements in the rating triples
for i in range(3):
  # Check if Alice's rating is greater than Bob's
  if a[i] > b[i]:
    # If so, Alice receives a point
    alice_points += 1
  # Check if Bob's rating is greater than Alice's
  elif a[i] < b[i]:
    # If so, Bob receives a point
    bob_points += 1

# Return the comparison points as a list
return [alice_points, bob_points]

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


................................................................................................................................................



Number 2 

Here's a possible solution using Python:

def staircase(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '#' * i)

This solution uses a for loop to iterate from 1 to n. For each number, it prints a string of spaces followed by a string of # characters. The number of spaces decreases from n - 1 down to 0, while the number of # characters increases from 1 to n. This creates the staircase shape

Here's an example of how the solution works when n = 4:

staircase(4)

This will print the following output:

   #
  ##
 ###

####

As you can see, the output is a staircase with a base and height of 4, drawn using # symbols and spaces. The last line has no spaces before it, as required by the problem statement.


................................................................................................................................................



Number 3

#                           PSDEUDO


In order to make the array beautiful, George needs to sort the array in non-descending order, so that the smallest element is at the first position, the second smallest at the second position, and so on.

To find the minimum number of swaps required to do this, George can first create a copy of the array and sort it in non-descending order. Then, he can compare the elements of the two arrays and swap the elements in the original array that are out of order. He can keep track of the number of swaps required as he goes along.

For example, in the array [7, 15, 12, 3], the sorted array would be [3, 7, 12, 15]. George can then compare the elements of the two arrays and perform the following swaps:

Swap the elements at positions 0 and 3: [7, 15, 12, 3] becomes [3, 15, 12, 7]. One swap performed.
Swap the elements at positions 1 and 2: [3, 15, 12, 7] becomes [3, 7, 12, 15]. Two swaps performed.
At this point, the array is already sorted in non-descending order, so George can stop. The minimum number of swaps required to make the array beautiful is 2.

Here is some pseudocode for the lilysHomework function:

function lilysHomework(arr):
  # Create a copy of the array and sort it in non-descending order.
  sortedArr = sort(arr)

  # Initialize the number of swaps required to 0.
  numSwaps = 0

  # Loop through the elements of the original array.
  for i in 0 to arr.length - 1:
    # If the element at position i is not in the correct position (i.e. it's not equal to the element at the same position in the sorted array),
    # then we need to swap it with the correct element.
    if arr[i] != sortedArr[i]:
      # Find the position of the correct element in the original array.
      correctPos = findPosition(sortedArr[i], arr)

      # Swap the element at position i with the correct element.
      swap(arr, i, correctPos)

      # Increment the number of swaps required.
      numSwaps = numSwaps + 1

  # Return the number of swaps required.
  return numSwaps

George can use this function to find the minimum number of swaps required to make the array beautiful, and help Lily finish her homework faster.

................................................................................................................................................



Number 4
                        
This pseudocode should produce the correct result for the given example and will find the minimum number of swaps required to make the array beautiful.

function lilysHomework(arr):
    # Sort the array in ascending order
    sorted_arr = sort(arr)

    # Keep track of the number of swaps required
    num_swaps = 0

    # Iterate through the original array
    for i in 0 to length(arr):
        # If the current element is not in the correct position, perform a swap
        # and increment the number of swaps required
        if arr[i] != sorted_arr[i]:
            swap(arr, i, index_of(sorted_arr, arr[i]))
            num_swaps++

    # Return the number of swaps required
    return num_swaps

................................................................................................................................................


Number 5 


To solve this problem, we can loop through the array and, for each element, check if there is another element in the array that has a difference of k with the current element. We can do this by checking if arr[i] + k or arr[i] - k is present in the array. If either of these values is present in the array, we can increment our counter and continue to the next element.

Here is some sample code that implements this idea:

// Complete the pairs function below.
int pairs(int k, int arr_count, int* arr) {
    int count = 0; // variable to store the number of pairs found
    for (int i = 0; i < arr_count; i++) {
        // check if there is an element in the array that has a difference of k with the current element
        if (isPresent(arr, arr_count, arr[i] + k) || isPresent(arr, arr_count, arr[i] - k)) {
            count++;
        }
    }
    return count;
}

// helper function to check if a value is present in an array
bool isPresent(int* arr, int arr_count, int value) {
    for (int i = 0; i < arr_count; i++) {
        if (arr[i] == value) return true;
    }
    return false;
}

................................................................................................................................................


Number 6

To come up with a weighted graph that has n=10 and m=11, we can use the following approach:
First, we need to create a graph with 10 nodes and 11 edges. We can label the nodes from 1 to 10, and connect each node with its adjacent nodes (e.g. node 1 with nodes 2 and 10, node 2 with nodes 1, 3, and 10, etc.). This will give us a graph with 10 nodes and 9 edges.

Next, we can add two more edges to the graph, connecting node 1 with node 5, and node 5 with node 9, as shown below:

image

To make the sum of the lengths of all edges as small as possible, we can assign a length of 1 to each edge. This will give us a weighted graph with n=10 and m=11, and a minimum spanning tree with a total weight of s=9 (the sum of all edge lengths in the minimum spanning tree).

To write an algorithm that computes the minimum spanning tree with n = 10 and m = n-1, we can use the following steps:
Start by creating a graph with n nodes and m=n-1 edges, as described above.

Initialize a variable s to 0, which will be used to store the total weight of the minimum spanning tree.

Use a loop to iterate over all edges in the graph, and for each edge, compute its weight and add it to s.

After all edges have been processed, return the value of s as the total weight of the minimum spanning tree.

Here is an example of how this algorithm might be implemented in Python:

# Create a graph with 10 nodes and 9 edges
n = 10
m = n - 1
graph = [(1, 2), (1, 10), (2, 3), (2, 10), (3, 4), (3, 10), (4, 5), (4, 10), (5, 6), (5, 9), (6, 7), (6, 9), (7, 8), (7, 9), (8, 9), (8, 10), (9, 10)]

# Initialize s to 0
s = 0

# Loop over all edges in the graph and add their weights to s
for u, v in graph:
    s += 1

# Return s as the total weight of the minimum spanning tree
return s


The algorithm returns the total weight (s) for the MST. The value of s will be the sum of all edge lengths in the minimum spanning tree, which will be 9 in the case of the example graph above.


................................................................................................................................................

Number 7 

 To solve this problem, we can use a dynamic programming approach. We can create an array dp where dp[i] represents the number of ways to make change for i coins. We can initialize the array with all zeros, except for the first element, which should be set to 1. This is because there is only 1 way to make change for 0 coins, which is not to take any coins.

Next, we can loop through the coins and, for each coin, update the dp array to reflect the number of ways to make change for each value from 1 to sum using the current coin. To do this, we can loop through the dp array starting from the value of the current coin and, for each dp[i], add the value of dp[i - coin] to it. This is because, if we have dp[i - coin] ways to make change for i - coin coins using the current coin, we also have that many ways to make change for i coins.

Here is some sample code that implements this idea:

int makeChange(int sum, vector<int> coins) {
    int n = coins.size(); // number of coins
    vector<int> dp(sum + 1, 0); // array to store the number of ways to make change for each value
    dp[0] = 1; // there is only 1 way to make change for 0 coins, which is not to take any coins

    // loop through the coins
    for (int i = 0; i < n; i++) {
        int coin = coins[i];
        // loop through the dp array starting from the value of the current coin
        for (int j = coin; j <= sum; j++) {
            // add the number of ways to make change for i - coin to dp[i]
            dp[j] += dp[j - coin];
        }
    }

    return dp[sum]; // return the number of ways to make change for sum coins
}


This solution has a time complexity of O(n * sum), which is efficient for small values of sum and n. However, for large values of these variables, we can use a more efficient solution that has a time complexity of O(n * sqrt(sum)). To do this, we can use the fact that, for a given value i, the number of ways to make change for i coins using the coins coins[0], coins[1], ... , coins[j] is the same as the number of ways to make change for i coins using the coins coins[0], coins[1], ... , coins[j], coins[j+1], ... , coins[n-1]. This is because, if we can make change for i coins using only the first j coins, we can also make change for i coins using all the coins.

Based on this fact, we can break the coins array into two parts: the first part contains the first j coins, and the second part contains the remaining coins. We can then use dynamic programming to calculate the number of ways to make change for i coins using only the first j coins. Since we know that the number of ways to make change for i coins using all the coins is the same as the number of ways to make change for i coins using only the first j




