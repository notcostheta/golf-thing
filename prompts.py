base = """
Parse the raw text event itinerary and generate a structured JSON response. Ensure the events are sorted by date and then by event start times. Handle missing data, multiple hosts, and events without end times.
Identify the following fields from the raw text:

Required fields for each event:
- `event_id`: Unique identifier.
- `date`: Date of the event.
- `title`: Event title.
- `start_time`: Start time.
- `end_time`: End time (if available).
- `duration`: Duration in minutes (if available).
- `host`: Host(s) as a list.
- `location`: Event location.
- `categories`: Categorize the Event in some form based on the potential attendee's demographic interest.
- `description`: Event description (if available).

Example Input:
Date: 27th April 2022

Event 1: Golf Tournament, 9:00 AM - 12:00 PM, Hosted by Tiger Woods and Lee Trevino, Location: Pine Valley Golf Course
Categories: Golf, Social
Description: Join Tiger Woods and other golf enthusiasts for a thrilling golf tournament.

Event 2: Welcome to the Conference, 10:00 AM, Hosted by Conference Chair, Location: Main Hall
Duration: 15 minutes
Categories: Social, Educational
Description: Get ready to kick off the conference with a warm welcome from our esteemed chair.

Date: 28th April 2022

Event 1: Keynote Speech, 9:30 AM - 10:30 AM, Hosted by Jane Doe, Location: Auditorium
Categories: Educational, Technology
Description: An inspiring talk on the future of AI in healthcare.

Example Output:
{
    "events": [
        {
            "event_id": "E001",
            "date": "27th April 2022",
            "title": "Golf Tournament",
            "start_time": "9:00 AM",
            "end_time": "12:00 PM",
            "duration": 180,
            "host": ["Tiger Woods", "Lee Trevino"],
            "location": "Pine Valley Golf Course",
            "categories": ["Golf", "Social"],
            "description": "Join Tiger Woods and other golf enthusiasts for a thrilling golf tournament."
        },
        {
            "event_id": "E002",
            "date": "27th April 2022",
            "title": "Welcome to the Conference",
            "start_time": "10:00 AM",
            "end_time": null,
            "duration": 15,
            "host": ["Conference Chair"],
            "location": "Main Hall",
            "categories": ["Social", "Educational"],
            "description": "Get ready to kick off the conference with a warm welcome from our esteemed chair."
        },
        {
            "event_id": "E003",
            "date": "28th April 2022",
            "title": "Keynote Speech",
            "start_time": "9:30 AM",
            "end_time": "10:30 AM",
            "duration": 60,
            "host": ["Jane Doe"],
            "location": "Auditorium",
            "categories": ["Educational", "Technology"],
            "description": "An inspiring talk on the future of AI in healthcare."
        }
    ]
}

Strictly return only the JSON response.
"""
