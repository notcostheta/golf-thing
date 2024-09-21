from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import json
from datetime import datetime
from models import Event, EventItinerary


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",  # Adjust this to your React frontend port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Helper function to parse custom date format
def parse_custom_date(date_string):
    return datetime.strptime(date_string, "%d %B %Y").strftime("%Y-%m-%d")


# Load events data
with open("data/events.json", "r") as f:
    events_data = json.load(f)

# Parse dates in the loaded data
for event in events_data["events"]:
    event["date"] = parse_custom_date(
        event["date"]
        .replace("th ", " ")
        .replace("st ", " ")
        .replace("nd ", " ")
        .replace("rd ", " ")
    )

# Sort events by date
events_data["events"].sort(key=lambda x: x["date"])


# Endpoint to get all events
@app.get("/events", response_model=EventItinerary)
async def get_events():
    return EventItinerary(events=[Event(**event) for event in events_data["events"]])


# Endpoint to get events for a specific date
@app.get("/events/{date}", response_model=EventItinerary)
async def get_events_by_date(date: str):
    events_for_date = [
        Event(**event) for event in events_data["events"] if event["date"] == date
    ]
    if events_for_date:
        return EventItinerary(events=events_for_date)
    raise HTTPException(status_code=404, detail="Date not found")


# Endpoint to get a specific event by event_id
@app.get("/event/{event_id}", response_model=Event)
async def get_event_by_id(event_id: str):
    for event in events_data["events"]:
        if event["event_id"] == event_id:
            return Event(**event)
    raise HTTPException(status_code=404, detail="Event not found")
