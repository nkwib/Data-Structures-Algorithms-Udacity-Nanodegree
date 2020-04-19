## Problem 2
##### Time Complexity: O(log(n)) where n is the number in the input_list
##### Space Complexity: O(1)

The algorithm is an adapted binary search that has an extra check at the moment of changing the first and last element of the interval where the search will be done.
The extra check doesn't affect the overall performance of the binary search and so the time complexity is O(log(n)) while the Space complexity is O(1) since the search is done in the original list.