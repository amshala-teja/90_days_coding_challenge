 - eventhough its a tree, since the infection is spread to both the parent and child, we treat it as an undirected graph

 - hence we should build an adjacency matrix
 - for that we need to import default dict from collections
 - lets make use of BFS, from the node with start
 - infect all nodes level by level
 - and lets keep track of time using the levels
 - track visited nodes to prevent revisiting
 