"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ["search_venues", "get_venue_details"]

QUERY_1_VENUE_NAME    = "The Haymarket Vaults"
QUERY_1_VENUE_ADDRESS = "1 Dalry Road, Edinburgh"
QUERY_2_FINAL_ANSWER  = "None of the available venues meet the criteria. The Albanach is full, so the agent reported 0 matches for 300 guests with vegan options."

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
When I changed The Albanach's status to 'full' in `mcp_venue_server.py`,
the agent in Query 1 automatically fell back to the next best match
(The Haymarket Vaults) without requiring any code changes in the LangGraph
client (`exercise4_mcp_client.py`). The client dynamically read the updated
response from the MCP server.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 130   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 0     # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP buys language-agnostic tool discovery and execution. The client doesn't need
to know the tools' implementation details, parameters, or even what language
they are written in. It simply connects to the server, queries the available
tools, and the server executes them locally, standardizing the tool interface
across multiple agents.
"""

# ── PyNanoClaw architecture — SPECULATION QUESTION ─────────────────────────
#
# (The variable below is still called WEEK_5_ARCHITECTURE because the
# grader reads that exact name. Don't rename it — but read the updated
# prompt: the question is now about PyNanoClaw, the hybrid system the
# final assignment will have you build.)
#
# This is a forward-looking, speculative question. You have NOT yet seen
# the material that covers the planner/executor split, memory, or the
# handoff bridge in detail — that is what the final assignment (releases
# 2026-04-18) is for. The point of asking it here is to check that you
# have read PROGRESS.md and can imagine how the Week 1 pieces grow into
# PyNanoClaw.
#
# Read PROGRESS.md in the repo root. Then write at least 5 bullet points
# describing PyNanoClaw as you imagine it at final-assignment scale.
#
# Each bullet should:
#   - Name a component (e.g. "Planner", "Memory store", "Handoff bridge",
#     "Rasa MCP gateway")
#   - Say in one clause what that component does and which half of
#     PyNanoClaw it lives in (the autonomous loop, the structured agent,
#     or the shared layer between them)
#
# You are not being graded on getting the "right" architecture — there
# isn't one right answer. You are being graded on whether your description
# is coherent and whether you have thought about which Week 1 file becomes
# which PyNanoClaw component.
#
# Example of the level of detail we want:
#   - The Planner is a strong-reasoning model (e.g. Nemotron-3-Super or
#     Qwen3-Next-Thinking) that takes the raw task and produces an ordered
#     list of subgoals. It lives upstream of the ReAct loop in the
#     autonomous-loop half of PyNanoClaw, so the Executor never sees an
#     ambiguous task.

WEEK_5_ARCHITECTURE = """
- The Autonomous Research Agent runs the open-ended LangGraph loop to explore,
search venues, calculate costs, and check weather, acting as the research half
of PyNanoClaw.
- The Shared MCP Server sits between the halves, exposing standardized tools
(like web search or venue booking) to both the LangGraph and Rasa agents.
- The Structured Confirmation Agent runs in Rasa CALM to securely and
deterministically enforce business constraints when on a live call with the pub
manager, forming the structured half of PyNanoClaw.
- The Memory Store uses a vector database (Pinecone) to provide RAG capabilities
so the autonomous agent can recall previous venue preferences or historical
event data.
- The Handoff Bridge connects the two halves, allowing the autonomous loop
to pass its researched context safely into the structured agent's strict dialog
flows before the live call begins.
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
The LangGraph agent is perfect for research because it can dynamically pivot,
as seen in Task C when it methodically checked every venue until finding
an available one. The Rasa CALM agent is essential for the call because it
enforces deterministic rules; swapping them feels wrong because you don't want
a creative LLM improvising a binding legal deposit limit, nor do you want
a rigid state machine struggling to search an open-ended database.
"""