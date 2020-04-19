
## problem 2
##### Time Complexity: O(n) where n=number of terminal nodes
##### Space Complexity: O(n) where n=number of files with requested extension

A basic recursive function that call itself if the path is a folder. recursive functions are ideal for these cases since there's no limit to the levels beneath every folder.

the time complexity depends on the numbers of terminal files at the very end of every path. Furthermore since this is a recursive function, everytime we call itself we are adding a call to the callstack. this can be extremely resource consuming for a directory that has many subdirectories because we have to walk the entirity of the possibilities in a path before removing the call from the call stack. Nonetheless the only solution is to check each file extension and, in case it's a folder, the entirity of its files.
The space complexity really depends on the number of found files since it's a simple list where we add the files that correspond to the requirements.