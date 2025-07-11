#!/bin/sh
uv run -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 