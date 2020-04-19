## Problem 7
##### Time Complexity: O(n)
##### Space Complexity: O(1) for lookup and O(n) for insertion of new nodes

As well as in problem 5, the data_structure used is a Trie. The main difference is that instead of letters we have the sub-domains that take us to a specific handler.
Insertion-wise the time and space complexity is O(n) where n is the number of sub-domains, since we are adding a key to a dictionary for each sub-domain.

the find method instead has the same time complexity since we have to walk down a branch that has as many nodes as the path has sub-domains. the space complexity is O(1) because we are not creating any new data.