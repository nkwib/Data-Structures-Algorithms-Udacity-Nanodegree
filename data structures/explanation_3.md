
## problem 3
##### Time Complexity: O(nlogn) where n=length of data
##### Space Complexity: O(n) where n = number of elements in the huffman tree

Since the "additional explanation" link was broken I looked over the internet for some other versions of the pseudocode to better understand the algorithm. I've seen that the majority of the time the tree implementation was done by using heapq and so I did the same.

Everything can be tested using the test function that returns the print statements of the boilerplate and if the code "passed" or "failed".

After checking some edge cases `(data = None | data = '')`, I call the encode function which create the tree and from the tree generated it assigns to each char a binary code from a map created by the function `map_characters`. after encoding each character with its correspondent one in the map created, I save the encoded data and the tree.

the decodification of the data is done from the binary string and the tree by walking through the tree adding a letter every time that we are on a "leaf". There's probably a better way of doing this by mapping the characters already found in a dictionary but I thought that the efficiency was already decent.

The time efficiency of this algorithm is O(nlogn) since it's O(logn) for the priority queue and O(n) for the `for loop` to map each character to its binary correspondent.
