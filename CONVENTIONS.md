# Conventions

**Note:** The primary development environment for this project is macOS. Scripts and instructions in this document use Unix/macOS conventions.

## Python Development

- **Dependency Management & Environments:**  
  Use [uv](https://github.com/astral-sh/uv) exclusively for creating virtual environments and managing dependencies.  
  - Declare dependencies in `pyproject.toml` (not requirements.txt).
  - Install all dependencies with `uv sync`.
  - Add new dependencies with `uv add <package>`.
  - Do not use pip or requirements.txt for any purpose.

- **Linting & Formatting:**  
  Use [ruff](https://github.com/astral-sh/ruff) for all linting and formatting tasks.  
  - Do not use other linters or formatters (e.g., flake8, black, isort) unless explicitly requested.

## Frontend

- React with TypeScript (see `frontend/` for details).

## AI/Automation

- The AI assistant should follow the above rules for all Python-related tasks.
