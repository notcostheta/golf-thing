import json
import dateparser
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from models import Event, EventItinerary, validate_json
from groq_client import get_groq_response, get_json_response
from prompts import base, condensed
from pdf_extractor import extract_text_from_pdf

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
    return dateparser.parse(date_string).strftime("%Y-%m-%d")


# Load events data
with open("data/events.json", "r") as f:
    events_data = json.load(f)

# Parse dates in the loaded data
for event in events_data["events"]:
    event["date"] = parse_custom_date(event["date"])

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


# Endpoint to upload a PDF and extract its contents
@app.post("/upload_pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        # Read the uploaded PDF file
        pdf_content = await file.read()
        text = extract_text_from_pdf(pdf_content)

        # Process the extracted text using Groq API
        resp = get_groq_response(
            model="llama-3.1-70b-versatile",
            messages=[
                {"role": "system", "content": condensed},
                {"role": "user", "content": text},
            ],
            temperature=0,
            max_tokens=8000,
        )

        thing_content = resp.choices[0].message.content

        # Retry validation up to 3 times
        max_retries = 3
        errors = []
        for attempt in range(max_retries):
            try:
                json_thing = get_json_response(
                    model="llama-3.1-70b-versatile",
                    messages=[
                        {"role": "system", "content": base},
                        {"role": "user", "content": thing_content},
                    ],
                    response_format={"type": "json_object"},
                    temperature=0,
                    max_tokens=8000,
                )

                json_thing_content = json.loads(json_thing.choices[0].message.content)

                validated_itinerary = validate_json(json_thing_content)
                if validated_itinerary:
                    return {
                        "status": "success",
                        "thing_content": thing_content,
                        "json_thing_content": validated_itinerary.dict(),
                    }
            except Exception as e:
                errors.append(str(e))
                # Modify the messages list to include the error
                thing_content += f"\nError: {str(e)}"
                if attempt < max_retries - 1:
                    continue
                else:
                    return {
                        "status": "error",
                        "message": "Validation failed after multiple attempts",
                        "thing_content": thing_content,
                        "json_thing_content": json_thing_content,
                        "errors": errors,
                    }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Run the application with Uvicorn
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
