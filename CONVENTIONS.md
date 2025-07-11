# Conventions

**Note:** The primary development environment for this project is macOS. Scripts and instructions in this document use Unix/macOS conventions.

## Table of Contents

- [Conventions](#conventions)
  - [Table of Contents](#table-of-contents)
  - [General](#general)
  - [Python Development](#python-development)
    - [Dependency Management \& Environments](#dependency-management--environments)
    - [Linting \& Formatting](#linting--formatting)
  - [Typing Conventions](#typing-conventions)
  - [Frontend](#frontend)
  - [AI/Automation](#aiautomation)

---

## General

- All scripts and instructions assume a Unix/macOS environment.

---

## Python Development

### Dependency Management & Environments

- Use [uv](https://github.com/astral-sh/uv) exclusively for creating virtual environments and managing dependencies.
  - Declare dependencies in `pyproject.toml` (not requirements.txt).
  - Install all dependencies with `uv sync`.
  - Add new dependencies with `uv add <package>`.
  - **NEVER** use pip or requirements.txt for any purpose.

### Linting & Formatting

- Use [ruff](https://github.com/astral-sh/ruff) for all linting and formatting tasks.
  - Do not use other linters or formatters (e.g., flake8, black, isort) unless explicitly requested.

---

## Typing Conventions

- **Never use the old Python typing imports** (e.g., `from typing import List, Optional, Dict, ...`).
- **Always use modern built-in type annotations** (e.g., `list`, `dict`, `tuple`, `set`, etc.) as introduced in Python 3.9+.
- Example:
  - Good: `planets: list[Planet]`
  - Bad: `planets: List[Planet]`

---

## Frontend

- Use React with TypeScript (see `frontend/` for details).

---

## AI/Automation

- The AI assistant should follow the above rules for all Python-related tasks.
