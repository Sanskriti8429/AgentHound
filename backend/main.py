from pathlib import Path

from fastapi import FastAPI, HTTPException

from loader import load_testbed
from build_graph import build_graph
from pathfinding import add_influence_edges, find_ranked_paths

app= FastAPI(title= "AgentHound")

CONFIG_PATH= Path(__file__).parent/"config"/"testbed.yaml"
nodes, edges= load_testbed(str(CONFIG_PATH))
graph= add_influence_edges(build_graph(nodes, edges))

@app.get("/")
def root():
    return{"message": "AgentHound API is running"}

@app.get("/graph")
def get_graph():
    return{
        "nodes": [{"id": n, **data} for n, data in graph.nodes(data= True)],
        "edges": [
            {"source": s, "target": t, **data}
            for s,t, data in graph.edges(data=True)
        ],
    }
    
@app.get("/paths")
def get_paths(start: str, end: str):
    for name in (start, end):
        if name not in graph:
            raise HTTPException(status_code= 404, detail=f"Unknown node:{name}")
        
    ranked= find_ranked_paths(graph, start, end)
    return{
        "start": start,
        "end": end,
        "paths": [{"path": path, "score": score} for path, score in ranked],
    }