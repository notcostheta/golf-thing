from pydantic import BaseModel
from typing import List, Optional, Union


class Event(BaseModel):
    event_id: str
    date: str
    title: str
    start_time: str
    end_time: str
    duration: int
    host: Optional[Union[str, List[str]]] = None
    location: str
    categories: List[str]
    description: str


class EventItinerary(BaseModel):
    events: List[Event]
