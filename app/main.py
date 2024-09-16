from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Union
from datetime import datetime
import json

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

# Sample data structure similar to your events.json

events_data = json.loads(open("data/events.json").read())


# Pydantic models for data validation
class Event(BaseModel):
    event_id: str
    title: str
    start_time: str
    end_time: str
    duration: int
    host: Union[str, List[str]]
    location: str
    description: Union[str, None] = None


class DaySchedule(BaseModel):
    date: str
    events: List[Event]


# Endpoint to get all events
@app.get("/events", response_model=List[DaySchedule])
async def get_events():
    return events_data


# Endpoint to get events for a specific date
@app.get("/events/{date}", response_model=DaySchedule)
async def get_events_by_date(date: str):
    for day in events_data:
        if day["date"] == date:
            return day
    raise HTTPException(status_code=404, detail="Date not found")


# Endpoint to get a specific event by event_id
@app.get("/event/{event_id}", response_model=Event)
async def get_event_by_id(event_id: str):
    for day in events_data:
        for event in day["events"]:
            if event["event_id"] == event_id:
                return event
    raise HTTPException(status_code=404, detail="Event not found")
