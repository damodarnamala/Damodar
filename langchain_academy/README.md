# LangChain Academy — Offline HTML Course

## Open the website
Unzip the archive. Open `langchain_academy/index.html` in Chrome, Firefox, Edge or Safari. All lesson, project, glossary, reference and learning path routes are **relative `.html` links**, so they work without hosting.

Optional local web server:
```sh
cd langchain_academy
python -m http.server 8000
```
Then visit http://localhost:8000/.

## Includes
- 19 topic modules, each with explanations, plain-language algorithm, architecture/data-flow diagram, concepts, Python snippet, execution discussion, mistakes, quizzes and exercise.
- 10 project briefs with implementation plans and test considerations.
- Syntax reference, glossary, learning path.
- Responsive sidebar search, code copy buttons, dark mode, local completion tracking.

## Running examples
Examples are provided for learning; they execute in your Python environment, not in the browser. Set up a Python virtual environment, install the packages shown on the homepage and in the module, and configure provider credentials. Some code snippets are deliberately conceptual pseudocode (explicitly labelled). API features may change; consult current documentation.

## Route integrity
Every href pointing within the website is a relative existing local file. External references are optional and require an internet connection.

## Security
Never paste actual API keys into browser source files or commit them to Git. Treat all model outputs and tool calls as untrusted until validated.

## References
https://docs.langchain.com/oss/python/langchain/overview
https://docs.langchain.com/oss/python/langgraph/overview
https://reference.langchain.com/python/langchain/agents/factory/create_agent
https://modelcontextprotocol.io/

Educational material authored for this request, October 2026.
