import yaml
from graph_model import Node, Edge

def load_testbed(path: str) -> tuple[list[Node], list[Edge]]:
    with open(path) as f:
        data= yaml.safe_load(f)
        
    nodes= [Node(**n) for n in data["nodes"]]
    edges= [Edge(**e) for e in data["edges"]]
    
    return nodes, edges

if __name__ == "__main__":
    nodes, edges= load_testbed("config/testbed.yaml")
    print(f"Loaded {len(nodes)} nodes, {len(edges)} edges")
    print(nodes[0])
    print(edges[0])