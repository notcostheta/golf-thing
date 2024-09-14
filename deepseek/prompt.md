### Generalized Prompt for Parsing Event Itinerary and Generating Structured Response

Parse a raw text event itinerary and generate a structured JSON response. Ensure the response is sorted by event start times. Handle missing data, multiple hosts, and events without end times.

Required fields:

- `event_id`: Unique identifier for the event.
- `title`: Title of the event.
- `start_time`: Start time of the event.
- `end_time`: End time of the event (if available).
- `duration`: Duration of the event (if available) in minutes.
- `host`: Host(s) of the event.
- `location`: Location where the event is held.
- `category`: Category of the event (e.g., Golf, Networking, Wellness, Promotional, Panel, Social, Educational).
- `description`: Description of the event.

Edge cases:

- Events without end times or durations: include only the start time in the 'start_time' field and set 'end_time' and 'duration' to null.
- Multiple hosts: include them as a list.
- Events with duration in minutes (e.g., 30 minutes, 45 minutes): convert to minutes for consistency.

Example raw text event itinerary:

Event 1: Golf Tournament, 9:00 AM - 12:00 PM, Hosted by Tiger Woods and Lee Trevino, Location: Pine Valley Golf Course
Description: Join Tiger Woods and other golf enthusiasts for a thrilling golf tournament.

Event 2: Welcome to the Conference, 10:00 AM, Hosted by Conference Chair, Location: Main Hall
Duration: 15 minutes

Event 3: Lunch Break, 12:00 PM - 1:30 PM, Location: Grand Ballroom
Description: Take a break and enjoy a meal with fellow attendees.

Event 4: Brainstorming Session, 2:00 PM - 3:45 PM, Led by Jane Doe and John Smith, Location: Innovation Hub
No description available.

Event 5: Gala Dinner, 7:00 PM - 10:00 PM, Hosted by Emily Davis, Location: Sky Lounge
Description: Join us for a night of food, drinks, and celebration.

### Structured JSON Response

```json
[
    {
        "event_id": "E001",
        "title": "Golf Tournament",
        "start_time": "9:00 AM",
        "end_time": "12:00 PM",
        "duration": 180,
        "host": ["Tiger Woods", "Lee Trevino"],
        "location": "Pine Valley Golf Course",
        "category": "Golf",
        "description": "Join Tiger Woods and other golf enthusiasts for a thrilling golf tournament."
    },
    {
        "event_id": "E002",
        "title": "Welcome to the Conference",
        "start_time": "10:00 AM",
        "end_time": null,
        "duration": 15,
        "host": ["Conference Chair"],
        "location": "Main Hall",
        "category": "Social",
        "description": "Get ready to kick off the conference with a warm welcome from our esteemed chair."
    },
    {
        "event_id": "E003",
        "title": "Lunch Break",
        "start_time": "12:00 PM",
        "end_time": "1:30 PM",
        "duration": 90,
        "host": ["Event Committee"],
        "location": "Grand Ballroom",
        "category": "Social",
        "description": "Take a break and enjoy a meal with fellow attendees."
    },
    {
        "event_id": "E004",
        "title": "Brainstorming Session",
        "start_time": "2:00 PM",
        "end_time": "3:45 PM",
        "duration": 105,
        "host": ["Jane Doe", "John Smith"],
        "location": "Innovation Hub",
        "category": "Educational",
        "description": "Join a dynamic discussion on innovative ideas and solutions."
    },
    {
        "event_id": "E005",
        "title": "Gala Dinner",
        "start_time": "7:00 PM",
        "end_time": "10:00 PM",
        "duration": 180,
        "host": ["Emily Davis"],
        "location": "Sky Lounge",
        "category": "Social",
        "description": "Join us for a night of food, drinks, and celebration."
    }
]
```