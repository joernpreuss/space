# space

## Backend (FastAPI)

1. Create and activate the virtual environment (if not already):

   ```sh
   uv venv
   source .venv/bin/activate
   ```

2. Install dependencies (if not already):

   ```sh
   uv add fastapi uvicorn ruff
   ```

3. Run the FastAPI server:

   ```sh
   uvicorn backend.main:app --reload
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
