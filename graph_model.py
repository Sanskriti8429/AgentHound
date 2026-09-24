from dataclasses import dataclass
from typing import Literal

@dataclass
class Node:
    id: str
    type: Literal["agent", "tool", "resource"]
    privilege: Literal["low", "medium", "high", "shared"]
    description: str=""
    
@dataclass
class Edge:
    source:str
    target: str
    kind: Literal["can_invoke", "can_delegate", "can_read", "can_write"]
    weight: int
    note: str= ""
    
    def crosses_trust_boundary(self) -> bool:
        return self.weight>0

if __name__ == "__main__":
    n=Node(id="research_agent", type="agent", privilege="low", description="Answers open web questions.")
    e=Edge(source="research_agent", target="shared_memory", kind="can_write", weight=2, note="Research agent writes untrusted content to shared memory.")
    print(n)
    print(e)