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

def find_all_paths(graph, start_node, end_node, path=None):
    """Return every simple path (no repeated nodes) from start_node to end_node."""
    if path is None:
        path=[]
    path= path+ [start_node]
    
    if start_node == end_node:
        return [path]
    
    if start_node not in graph:
        return[]
    
    paths=[]
    for neighbour in graph.successors(start_node):
        if neighbour not in path:
            new_paths= find_all_paths(graph, neighbour, end_node, path)
            paths.extend(new_paths)
            
    return paths

def score_path(graph, path):
    """Sum the trust-boundary weight of every edge along a path."""
    total=0
    for i in range(len(path)-1):
        source, target= path[i], path[i+1]
        edge_data= graph.get_edge_data(source, target)
        total += edge_data["weight"]
    return total

def find_ranked_paths(graph, start_node, end_node):
    """Find every path start->end, score each, return sorted most-to-least dangerous."""
    paths= find_all_paths(graph, start_node, end_node)
    scored= [(path, score_path(graph, path)) for path in paths]
    scored.sort(key= lambda item: item[1], reverse= True)
    return scored

if __name__ == "__main__":
    nodes, edges= load_testbed("config/testbed.yaml")
    graph= build_graph(nodes, edges)
    
    print("=== Dangerous routes to finance_db ===")
    ranked= find_ranked_paths(graph, "research_agent", "finance_db")
    for path, score in ranked:
        print(f"Score {score}: {'->'.join(path)}")
        
    print("\n=== Safe route to analytics_db ===")
    ranked_safe= find_ranked_paths(graph, "email_agent", "analytics_db")
    for path, score in ranked_safe:
        print(f"Score {score}: {'->'.join(path)}")