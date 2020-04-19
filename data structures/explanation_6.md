
## problem 6
##### Time Complexity: O(n) where n is the number of element in the longer list
##### Space Complexity: O(n) where n is the size of result list

the algorithms are optimized to be time efficient but they both used a dictionary to track down wich element has been added.
The union algorithm walk through the lists at the same time only once. if it sees a new element that is not in the dictionary, the element is added to the result list.
the intersection algorithm is a modified version of the union one. if it sees a new element, the new value is added as a key in the dictionary with the name of the list as a value while if the element is already present in the dictionary it is added to the final list only if the value is of the other list name.

the time complexity for both is O(n) where n is the number of element in the longer list