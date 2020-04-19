## Problem 5
##### Time Complexity: O(n) for lookup where n = searched string length 
##### Space Complexity: O(m*n) where m is the alphabet size and m the key_length
([source](https://www.geeksforgeeks.org/trie-insert-and-search/))

The data structure used is a Trie that in Python is implemented as a dictionary that contains a variable number of dictionaries in itself. this substructures are the nodes of the Trie and they can be variable in number. Walking down one of this branch we can retrieve the pieces of the data that we are looking for.

Tries are often used for the autocomplete feature of an application: if I digit for example "CO" the algorithm will position itself at the node "O" inside the node "C" and from there it will search every possible outcome of the branch that starts at "O" inside "C". We could find one node that represents "P" with the flag "finished_word" and the input will now suggest "COP". We can also assert that the children of a node are always limited in number because they cannot exceed the numbers of valid characters that will eventually form a word with that suffix.