# # def staircase(n):
# #     for i in range(n+1):
# #        print(' ' * (n - i) + '#' * i)
# # print(staircase(10))

# # $max=5;
# # for ( $i =1 ; $i<=$max;$i++) {
# #         for ( $space = 1; $space <= ($max-$i);$space++) {
# #                 echo " ";
# #         }
# #         for ( $hash = 1; $hash <= $i;$hash ++ ) {
# #                 echo "#";
# #         }
# #         echo "\n";
# # }

# # Consider a staircase of size :
# #    #
# #   ##
# #  ###
# # ####
# # Observe that its base and height are both equal to , and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.
# # Write a program that prints a staircase of size .
# # Function Description
# # Complete the staircase function in the editor below. It should print a staircase as described above.
# # staircase has the following parameter(s):
# # n: an integer
# # Input Format
# # A single integer, , denoting the size of the staircase.
# # Constraints
# #  .
# # Output Format
# # Print a staircase of size  using # symbols and spaces.
# # Note: The last line must have  spaces in it.
# # Sample Input
# # 6 
# # Sample Output
# #      #
# #     ##
# #    ###
# #   ####
# #  #####
# # ######
# # Explanation
# # The staircase is right-aligned, composed of # symbols and spaces, and has a height and width of 




# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# # Complete the staircase function below.
# def staircase(n):
#     for i in range(n+1):
#        print(' ' * (n - i) + '#' * i)
# print(staircase(10))

# $max=5;
# for ( $i =1 ; $i<=$max;$i++) {
#         for ( $space = 1; $space <= ($max-$i);$space++) {
#                 echo " ";
#         }
#         for ( $hash = 1; $hash <= $i;$hash ++ ) {
#                 echo "#";
#         }
#         echo "\n";
# }

# Consider a staircase of size :
#    #
#   ##
#  ###
# ####
# Observe that its base and height are both equal to , and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.
# Write a program that prints a staircase of size .
# Function Description
# Complete the staircase function in the editor below. It should print a staircase as described above.
# staircase has the following parameter(s):
# n: an integer
# Input Format
# A single integer, , denoting the size of the staircase.
# Constraints
#  .
# Output Format
# Print a staircase of size  using # symbols and spaces.
# Note: The last line must have  spaces in it.
# Sample Input
# 6 
# Sample Output
#      #
#     ##
#    ###
#   ####
#  #####
# ######
# Explanation
# The staircase is right-aligned, composed of # symbols and spaces, and has a height and width of 




# if __name__ == '__main__':
#     n = int(input())

#     staircase(n)

#     #                           PSDEUDO

if __name__ == '__main__':
    n = int(input())

    staircase(n)

    #                           PSDEUDO

# Loop over all edges in the graph and add their weights to s
for u, v in graph:
    s += 1

# Return s as the total weight of the minimum spanning tree
print (s)