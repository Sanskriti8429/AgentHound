from dataclasses import dataclass
from typing import Literal

@dataclass
class Node:
    id: str
    type: Literal["agent", "tool", "resource"]
    privilege: Literal["low", "medium", "high", "shared"]
    description: str=""
    
    
if __name__ == "__main__":
    n=Node(id="research_agent", type="agent", privilege="low", description="Answers open web questions.")
    print(n)