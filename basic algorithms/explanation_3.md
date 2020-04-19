
## Problem 3
##### Time Complexity: O(nlog(n)) where n is the number of the input_list
##### Space Complexity: O(n)

I assume that the list will always contain positive integers.

I've started to think that higher numbers have the digits with the higher values on the left side obviously. Furthermore the bigger the numbers that are added, the bigger the result.
So I decided to approach this problem using a merge-sort that has a complexity of O(nlog(n)) timewise and O(n) for the space.
after sorting and reversing the digits in the array I split the even digits and the odd ones so that the addition of the two numbers will always be the higher value possible.

The sorting algorithm is the one that gives to this problem its complexity for both space and time. it the input list would have been already sorted the space complexity would have been O(n) and the space complexity would have been O(1)