from collections import defaultdict, deque

# Function to load a list of edges into a graph.
def load_graph(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    return graph

# Kahn’s algorithm repeatedly removes nodes with in-degree 0, and guarantees a
# valid linear ordering of all vertices in a DAG. Returns a list topologically
# sorted, or raises a ValueError upon detecting a cycle.
def khan_topo_sort(g):
    # Calculate in-degree of each vertex, defaults to 0 for unspecified keys
    in_degree = defaultdict(int)
    for u in g:
        for v in g[u]:
            in_degree[v] += 1
    
    # Set up queue, and load with verticies of in-degree 0.
    queue = deque([node for node in g if in_degree[node] == 0])

    # Set up return list, and counter to help us detect cycles..
    topo_order = []
    removed = 0

    # Set up a loop to remove nodes of in-degree 0, putting them in queue. The
    # result is a topological ordering count of removed verticies.
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        removed += 1

        # For each neighbor of u, reduce it's (v's) in-degree.
        for v in g[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    # If the queue is done, but the graph still contains unprocessed data, this
    # indicates a loop, so we raise a ValueError.
    if removed != len(g):
        raise ValueError("Graph contains cycle, cannot sort topologically.")
    return topo_order

if __name__ == "__main__":

    # Set up two test lists of edges, one acyclic, and the other with a cycle
    # that should raise a ValueError.
    edges_valid = [
        (2, 3),
        (5, 0),
        (4, 0),
        (4, 1),
        (5, 2),
        (3, 1)
        ]
    edges_invalid = [
        (2, 3),
        (5, 0),
        (4, 0),
        (4, 1),
        (5, 2),
        (3, 2)
        ]
    
    # Load these into graphs.
    acyclic_graph = load_graph(edges_valid)
    cyclic_graph = load_graph(edges_invalid)

    # Let the user know what is being processed, and run the tests.
    print("Attempting to topologically sort the following acyclic graph:")
    print(acyclic_graph)
    try:
        order = khan_topo_sort(acyclic_graph) # Success!
        print("Topologically sorted order: ", order)
    except ValueError as e:
        print(e)
    print("Attempting to topologically sort the following cyclic graph:")
    print(cyclic_graph)
    try:
        order = khan_topo_sort(cyclic_graph) # ValueError!
        print("Topological ordering", order)
    except ValueError as e:
        print(e)