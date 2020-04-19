
## problem 4
##### Time Complexity: O(m*n) where m=number of groups and n=number of users
##### Space Complexity: O(n) where n is the number of call in the call stack

the structure of an active directory is a tree-shaped one. This algorithm is using depth first search to go through each node of the tree where the final nodes are the users.
The space complexity depens on the call stack that increases at each subgroup that call the recursive function.