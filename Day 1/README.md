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
 