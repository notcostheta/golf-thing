from pydantic import BaseModel, ValidationError
from typing import List, Optional


class Event(BaseModel):
    event_id: str
    date: str
    title: str
    start_time: str
    end_time: Optional[str] = None
    duration: Optional[int] = None
    host: Optional[List[str]] | str = None
    location: str
    categories: List[str]
    description: Optional[str] = None


class EventItinerary(BaseModel):
    events: List[Event]


def validate_json(json_data):
    try:
        event_itinerary = EventItinerary.model_validate(json_data)
        print("Validation successful!")
        return event_itinerary
    except ValidationError as e:
        print("Validation failed!")
        print(e.json())
        return None
