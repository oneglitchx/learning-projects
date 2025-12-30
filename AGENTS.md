# AGENTS.md

This file provides guidelines and commands for agents working in this repository. It includes build, lint, and test commands, as well as code style guidelines derived from analyzing the existing codebase.

## Build Commands

Since this is a Python project with mini-projects (scripts), there are no build commands. Run individual scripts directly with Python:

- Run a specific mini-project: `python python/mini-projects/calculator.py`
- Run experimentation: `python python/experimentation.py`

If adding a package later, install dependencies (if requirements.txt is added): `pip install -r requirements.txt`

## Lint Commands

Use standard Python linting tools to ensure code quality. Recommended tools:

- **flake8** for style and error checking: `flake8 .` (checks PEP8 compliance, errors, etc.)
- **black** for code formatting: `black .` (auto-formats code to consistent style)
- **mypy** for type checking (if type hints are added): `mypy .`

Run linting before committing: `flake8 . && black --check .`

## Test Commands

No tests are currently present in the codebase. When adding tests, use pytest:

- Run all tests: `pytest`
- Run tests in a specific directory: `pytest python/mini-projects/`
- Run a single test: `pytest test_file.py::test_function_name` (replace with actual file and function)
- Run tests with coverage: `pytest --cov=.`

Assume tests will be added in a `tests/` directory or alongside code files.

## Code Style Guidelines

These guidelines are inferred from the existing codebase and standard Python practices. Follow them for consistency.

### Imports

- Place all imports at the top of the file.
- Group imports: standard library first, then third-party, then local.
- Use absolute imports where possible.
- Example:

```python
import os
import json
import random

from pathlib import Path  # if needed
```

- Avoid wildcard imports (`from module import *`).
- Sort imports alphabetically within groups.

### Formatting

- Follow PEP8 for indentation, line length (79 chars), etc.
- Use 4 spaces for indentation (no tabs).
- Use Black for automatic formatting to ensure consistency.
- Blank lines: 2 between top-level functions/classes, 1 within functions.
- Trailing commas in lists/dicts for better diffs.

### Types

- Add type hints for function parameters and return values where clarity helps.
- Use `typing` module for complex types (List, Dict, etc.).
- Example:

```python
from typing import List, Dict

def add_tasks(tasks: List[str]) -> None:
    pass
```

- No type hints were used in existing code, but recommend adding them for new code.

### Naming Conventions

- Functions: snake_case (e.g., `add_task`, `view_tasks`)
- Variables: snake_case (e.g., `user_input`, `task_list`)
- Constants: UPPER_SNAKE_CASE (e.g., `MAX_ATTEMPTS`)
- Classes: PascalCase (if any, none in current code)
- Avoid camelCase (seen in some existing code like `addTasks` – refactor to `add_tasks`)
- Files: snake_case with .py extension (e.g., `todo_list.py`)

### Error Handling

- Use specific exceptions, not bare `except:`.
- Catch expected errors (e.g., `ValueError`, `FileNotFoundError`).
- Use try-except-else-finally as needed.
- Example (improving existing code):

```python
try:
    num = int(input("Enter number: "))
except ValueError:
    print("Invalid input, enter a number.")
else:
    print(f"Number: {num}")
```

- Avoid global exception handling that hides issues.

### Comments and Docstrings

- Use docstrings for functions: triple quotes explaining purpose, params, returns.
- Inline comments for complex logic.
- Keep comments concise and useful.
- Example:

```python
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        The sum of a and b
    """
    return a + b
```

### Functions and Structure

- Break code into functions for reusability.
- Avoid global variables; pass data as parameters.
- Use `if __name__ == "__main__":` for script entry points.
- Keep functions small and focused on one task.

### Strings and Output

- Use f-strings for formatting (preferred over .format() or %).
- For user-facing text, consider capitalization consistency (existing code uses .title() inconsistently – standardize).
- Avoid hardcoded strings; use constants if repeated.

### Data Structures

- Use lists for ordered collections.
- Use dicts for key-value data (as in quiz.json handling).
- Prefer comprehensions for simple transformations.

### File Handling

- Use `with` statements for file operations to ensure closing.
- Handle file existence checks properly (as in existing code).
- Use JSON for data persistence (as in quiz and rock-paper-scissors).

### Miscellaneous

- Avoid magic numbers; use named constants.
- Write readable code; prioritize clarity over cleverness.
- Test edge cases in logic.
- Emojis: Use sparingly in output, only if enhancing UX (seen in quiz.py).

### Cursor Rules

No .cursorrules or .cursor/rules/ found in the repository.

### Copilot Rules

No .github/copilot-instructions.md found in the repository.

If adding these files, include their contents here for reference.

## Additional Notes

- The codebase consists of simple Python scripts for learning mini-projects.
- No CI/CD setup; run commands manually.
- When adding dependencies, create requirements.txt.
- For version control: Commit after linting and testing.
- Follow git best practices: descriptive commits, small changes.</content>
<parameter name="filePath">AGENTS.md