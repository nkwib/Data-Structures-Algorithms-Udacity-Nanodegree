
## Problem 4
##### Time Complexity: O(n) where n is the number of the input_list
##### Space Complexity: O(1)

The algorithm sorts in place the array of 0,1,2 using the logic of moving the 0 to the left, the 2 to the right and doing nothing if there's a one.

By walking through the list we are able to modify the list as we go by without using any other variable and in one pass. the time complexity is o(n) since we have to walk the whole list at least once. the time complexity is O(1)