# Depth-First Search (DFS) - Iterative Approach(深度優先搜尋-迭代法)
def dfs_iterative(graph, start):
    # Initialize an empty set to keep track of visited nodes to avoid infinite loops
    visited = set()
    
    # Initialize a stack with the starting node
    stack = [start]
    
    # Continue searching as long as there are nodes in the stack
    while stack:
        # Remove and return the last element added to the stack (LIFO)
        node = stack.pop()
        
        # Check if the node has been visited before
        if node not in visited:
            # Print the current node (or perform other operations)
            print(node, end=" ")
            
            # Mark the current node as visited
            visited.add(node)
            
            # Add all unvisited neighbors of the current node to the stack
            # Note: The order in the stack determines the next node to visit
            stack.extend(graph[node])

# Define the graph using an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Execute the DFS starting from node 'A'
# Output: A C F E B D 
dfs_iterative(graph, 'A')