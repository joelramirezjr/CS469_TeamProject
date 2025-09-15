# Function for topological sort using a DFS-based approach.
def dfs_topological_sort(graph):
    # A dictionary to keep track of the state of each node:
    # 0-unvisited, 1-visiting (current recursion stack), 2-visited (explored all neighbors)
    visited_states = {node: 0 for node in graph}
    # List to store the sorted nodes
    topo_order = []

    # Recursive sort function
    def dfs(node):
        # Mark the node as 'visiting'
        visited_states[node] = 1  

        # Explore the neighbors of the current node
        for neighbor in graph.get(node, []):
            if visited_states[neighbor] == 1:
                # Detects a cycle if an already-visited neighbor
                raise ValueError("Graph contains cycle.")
            if visited_states[neighbor] == 0:
                # If neighbor is unvisited, recurse on it
                dfs(neighbor)
        # Mark the node as 'visited' and add the node to the front of the list
        visited_states[node] = 2  
        topo_order.insert(0, node)

    # Iterate through all nodes to ensure all components of the graph are visited
    try:
        for node in graph:
            if visited_states[node] == 0:
                dfs(node)
    except ValueError as e:
        print(f"Error: {e}")
        return None

    return topo_order


if __name__ == "__main__":
    # Simple set
    graph_1 = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    print("Attempting to sort Graph 1...")
    print(f"Graph 1 sorted order: {dfs_topological_sort(graph_1)}")

    # Complex set
    graph2 = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['E', 'F'],
        'D': ['G'],
        'E': ['G', 'H'],
        'F': ['H'],
        'G': [],
        'H': []
    }
    print("Attempting to sort Graph 2...")
    print(f"Graph 2 sorted order: {dfs_topological_sort(graph2)}")

    # Example 3: A graph with a cycle
    graph3 = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A']
    }
    # This will print "Error: Graph contains cycle." then return None for the sorted order.
    print("Attempting to sort Graph 3...")
    print(f"Graph 3 sorted order: {dfs_topological_sort(graph3)}") 