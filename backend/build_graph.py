import networkx as nx
from graph_model import Node, Edge

def build_graph(nodes: list[Node], edges: list[Edge]) -> nx.DiGraph:
    graph= nx.DiGraph()
    
    for node in nodes:
        graph.add_node(node.id, type=node.type, privilege=node.privilege, description= node.description)
        
    for edge in edges:
        graph.add_edge(edge.source, edge.target, kind=edge.kind, weight=edge.weight, note=edge.note)
        
    return graph

if __name__ == "__main__":
    nodes=[
        Node(id="research_agent", type="agent", privilege="low", description="Answers open web questions."),
        Node(id="shared_memory", type="resource", privilege="shared", description="Shared scratchpad all agents can write to."),
    ]
    
    edges=[
        Edge(source="research_agent", target="shared_memory", kind="can_write", weight=2, note="Research agent writes untrusted content to shared memory."),
    ]
    
    graph= build_graph(nodes,edges)
    
    print("Nodes:\n", graph.nodes(data=True))
    print("\nEdges:\n", graph.edges(data=True))