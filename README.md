# AgentHound

A graph-based attack-path mapper for multi-agent AI systems, inspired by BloodHound (the active directory attack-path tool used widely in offensive security).

## What this is

AgentHound models a multi-agent AI system- agents, tools, and shared resources- as a directed graph, then analyzes it to find privilege-escalation paths: routes by which a low-privilege agentcould indirectly trigger a high-privilege action (e.g. via shared memory an orchestrator agent trusts).

## Status

* In active development.

- [x] Graph data model (nodes, edges, trust boundaries)
- [ ] Path-finding engine (BFS + weighted ranking by trust boundary crossings)
- [ ] Multi-agent testbed (LangChain + Ollama)
- [ ] Instrumented edge capturefrom real agent execution
- [ ] Red-team demo: predicted vs. executed prompt-injection attack path
- [ ] D3.js interactive graph viewer

## Why this exists

Most AI-agent-security tooling right now focuses on guardrails and prompt filters. Almost nothing maps the *structural* attack surface - which agent can reach which tool or resource, indirectly, through delegation and shared state - the way BloodHound does for identity/AD environments.

## Stack

Python | NetworkX | LangChain | Ollama (local LLM) | D3.js

## Setup

\'\'\'bash
python -m venv venv
venv\Scripts\activate #Windows
pip install -r requirements.txt
\'\'\'