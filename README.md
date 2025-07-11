# Project "space"

**Note:** The primary development environment for this project is macOS. Scripts and instructions in this README use Unix/macOS conventions.

## Backend (FastAPI)

1. Run the backend server (recommended):

   For development:

   ```sh
   ./run_backend_dev.sh
   ```

   For production:

   ```sh
   ./run_backend_prod.sh
   ```

   (Alternatively, you can run uvicorn directly:)

   ```sh
   uv run -m uvicorn backend.main:app --reload
   ```

2. (Optional) Activate the environment if you want to run Python commands directly:

   ```sh
   source .venv/bin/activate
   ```

## Frontend (React + TypeScript)

1. Install dependencies:

   ```sh
   cd frontend
   npm install
   ```

2. Start the development server:

   ```sh
   npm start
   ```

The React app will run on [http://localhost:3000](http://localhost:3000) and the FastAPI backend on [http://localhost:8000](http://localhost:8000) by default.
