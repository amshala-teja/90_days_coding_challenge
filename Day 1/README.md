# LC 2385
 
 - eventhough its a tree, since the infection is spread to both the parent and child, we treat it as an undirected graph

 - hence we should build an adjacency matrix
 - for that we need to import default dict from collections
 - lets make use of BFS, from the node with start
 - infect all nodes level by level
 - and lets keep track of time using the levels
 - track visited nodes to prevent revisiting

# LC 26

 - its a simple array problem to remove the duplicates inplace
 - used a two pointer technique 
 - since the array is sorted
 - One pointer i traverses the entire array.
 - The other pointer j keeps track of the position where the next unique element should be placed.
 - j starts at position 1 because the first element is always unique.
 - Loop through the array starting from index 1.
 - If the current element nums[i] is different from the previous element nums[i - 1], it is a unique element.
 - Place this unique element at position j.
 - Move j forward to prepare for the next unique element.


# LC 27
 - This solution uses the two-pointer technique:
 - One pointer i traverses the entire array.
 - The other pointer j keeps track of where the next valid (non-val) element should be placed
 - remaning is simalar to the aboce LC 26

# LC 344

 - here we use two pointer technique
 - will take one pointer at the start and one on the end and swap the values in plae
 - increment i and decrement j by 1 using while "i < j"
 - return string

# LC 283

 - Here also we used two pointer technique.
 - i to iterate through the entire array.
 - j to track the position where the next non-zero element should be placed.
 - Swap elements when a non-zero is encountered to gradually shift all zeros to the end.