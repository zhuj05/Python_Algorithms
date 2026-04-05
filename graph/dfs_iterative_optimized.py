def dfs_iterative_optimized(graph, start_node):
    # Optimization 2: Check for empty graph
    if not graph or start_node not in graph:
        return []

    visited = set()
    # Optimization 3: Use a local list for faster access than global scope
    stack = [start_node]
    result = []
    
    # Avoid re-evaluating 'stack' length in every iteration
    # Use 'while stack' as it's the most "Pythonic" and fastest
    while stack:
        node = stack.pop()
        
        if node not in visited:
            visited.add(node)
            result.append(node)
            
            # Optimization 4: List comprehension/Reversed filtering
            # We push neighbors in reverse to maintain expected traversal order
            neighbors = [n for n in graph.get(node, []) if n not in visited]
            stack.extend(reversed(neighbors))
            
    return result

# Define the graph using an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


output = dfs_iterative_optimized(graph, 'A')
print(f"DFS result: {output}")
# output
# DFS result: ['A', 'B', 'D', 'E', 'F', 'C']