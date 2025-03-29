from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://alexpi44.github.io"  # ✅ Your GitHub Pages domain
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Your existing route
from pathlib import Path
import json
from fastapi.responses import JSONResponse

@app.get("/events")
def get_events():
    data_path = Path(__file__).parent.parent / "data" / "events.json"
    with open(data_path, "r") as f:
        data = json.load(f)
    return JSONResponse(content=data)
