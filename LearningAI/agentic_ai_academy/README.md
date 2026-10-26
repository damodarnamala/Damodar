# Agentic AI Academy — Offline HTML Tutorial

A static, browsable 30-module Agentic AI curriculum with searchable navigation, concepts, algorithms, Python snippets, exercises, 10 project guides, setup, and a syntax reference. Open `index.html` directly in a browser. No web server is required.

## Quick start
1. Unzip.
2. Open `index.html`.
3. Read `setup.html` before executing code.
4. Create a Python virtual environment (Python 3.11+ recommended).
5. Run `python examples/01_agent_loop.py` and `python -m unittest discover -s examples -p 'test_*.py'`.
6. Optionally `pip install -r requirements-optional.txt` to run SDK examples.

## Layout
- `index.html`: course home
- `lessons/01.html`–`lessons/30.html`: lesson pages
- `setup.html`: configuration instructions
- `projects.html`: guided assignments and AI software factory workflow
- `reference.html`: API cheat sheet and official documentation
- `examples/`: Python sample source files
- `docs/`: supplementary explanatory documents

## Scope
The course teaches concepts and provides representative runnable code. Some advanced topics and enterprise projects are guided builds/design exercises rather than full production implementations. No secrets, external service accounts, or deployment integration are preconfigured.

## Version note
Prepared October 2026. Always check the latest official SDK API references before production integration. The LangGraph prebuilt `create_react_agent` is deprecated in favor of `langchain.agents.create_agent` for modern high-level agent construction.
