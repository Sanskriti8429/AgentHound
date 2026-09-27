import networkx as nx
from graph_model import Node, Edge
from loader import load_testbed

def build_graph(nodes: list[Node], edges: list[Edge]) -> nx.DiGraph:
    graph= nx.DiGraph()
    
    for node in nodes:
        graph.add_node(node.id, type=node.type, privilege=node.privilege, description= node.description)
        
    for edge in edges:
        graph.add_edge(edge.source, edge.target, kind=edge.kind, weight=edge.weight, note=edge.note)
        
    return graph

if __name__ == "__main__":
    nodes, edges= load_testbed("config/testbed.yaml")
    graph= build_graph(nodes,edges)
    
    print(f"Graph has {graph.number_of_nodes()} nodes and {graph.number_of_edges()} edges")
    print("Nodes:\n", graph.nodes(data=True))
    print("\nEdges:\n", graph.edges(data=True))