# AgentHound

**Graph-based attack-path analysis for multi-agent AI systems.**

AgentHound models the agents, tools, and shared resources of an AI system as a directed graph, then finds and ranks the routes by which a low-privilege agent could trigger a high-privilege action. It is inspired by BloodHound's approach to Active Directory.

## Overview

Multi-agent systems delegate tasks, spawn sub-agents, call tools, and share memory. Each of these is a trust relationship, and chains of them create escalation paths that no one designed and no one reviews. AgentHound makes those paths visible and ranks them by risk.

## Features

- **Declarative system model.** Describe agents, tools, resources, and their capabilities in YAML.
- **Weighted trust graph.** Edges are typed (`can_invoke`, `can_delegate`, `can_spawn`, `can_read`, `can_write`) and weighted by the trust boundary they cross.
- **Indirect influence detection.** Derives `can_influence` edges wherever one agent writes to a shared resource that another reads, which is the mechanism behind prompt injection through shared memory.
- **Path analysis.** Enumerates every route from low-privilege agents to crown-jewel targets and ranks them by cumulative risk. Also computes the safest route with Dijkstra's algorithm for comparison.
- **REST API.** FastAPI backend exposing the graph and the analysis.

## Example Finding

```
research_agent -> orchestrator_agent -> audit_agent -> finance_db    risk score: 18
```

A low-privilege research agent writes to shared memory. The orchestrator reads it as trusted input and spawns a high-privilege audit agent, which has direct access to the production database.

## Architecture

```
testbed.yaml  ->  loader  ->  graph builder  ->  path analysis  ->  REST API  ->  visualization
```

## Roadmap

- [x] Graph data model and YAML loader
- [x] Path-finding engine (BFS, all-paths enumeration, Dijkstra, risk ranking, derived `can_influence` edges)
- [x] FastAPI backend (`/graph`, `/paths`, `/analyze`)
- [ ] Multi-agent testbed (LangChain + Ollama)
- [ ] Instrumented edge capture from real agent execution
- [ ] Red-team validation: predicted vs. executed prompt-injection attack path
- [ ] D3.js interactive graph viewer

## Tech Stack

Python, NetworkX, FastAPI, LangChain, Ollama, D3.js

## Getting Started

```bash
git clone https://github.com/Sanskriti8429/AgentHound.git
cd agenthound
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
cd backend
python -m uvicorn main:app --reload
```

API documentation is served at `/docs` once the server is running.