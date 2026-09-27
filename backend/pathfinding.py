from collections import deque
from loader import load_testbed
from build_graph import build_graph

def bfs_reachable(graph, start_node):
    """Return the set of all nodes reachable from start_node, ignoring weights."""
    visited = {start_node}
    queue= deque([start_node])
    
    while queue:
        current= queue.popleft()
        for neighbour in graph.successors(current):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                
    return visited

if __name__ == "__main__":
    nodes, edges= load_testbed("config/testbed.yaml")
    graph= build_graph(nodes, edges)
    
    reachable= bfs_reachable(graph, "research_agent")
    print("Reachable from research_agent:")
    for node in reachable:
        print(" -", node)