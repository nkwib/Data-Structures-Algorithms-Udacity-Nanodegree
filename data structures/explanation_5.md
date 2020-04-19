
## problem 5
##### Time Complexity: O(1) to insert an element
##### Space Complexity: O(n) where n is the size of the Blockchain

The block of the chain have the timestamp of their creation, the data stored, a reference to the previous Block (like a linked list), a copy of the previous Block hash and a hash based on the data the timestamp contained.
Like in a linked list, the creation of a block has a time complexity of O(1). In the test I've implemented a function that lists all the Blocks created and it has a time complexity of O(n) where n is the numbers of Block of the Blockchain.
