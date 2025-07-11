import os
from datetime import datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session

from backend.db_utils import create_db_and_tables, get_engine
from backend.planet_data import insert_star_system


# --- Database Setup ---
def get_database_url() -> str:
    return os.getenv("DATABASE_URL", "sqlite:///astronomy.db")


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"Hello from FastAPI!\nCurrent server time: {current_time}"
    return {"message": message}


if __name__ == "__main__":
    engine = get_engine(get_database_url())
    create_db_and_tables(engine)
    with engine.begin() as conn:
        with Session(conn) as session:
            insert_star_system(session)
