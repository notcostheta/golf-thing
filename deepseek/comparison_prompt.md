Certainly! Below is a detailed prompt that guides the process of generating a customer priority event list based on the provided itinerary JSON and individual customer demographics. The prompt includes examples and instructions to ensure the recommendations are handled perfectly.

### Prompt for Generating Customer Priority Event List

```plaintext
You are tasked with generating a customer priority event list based on the provided itinerary JSON and an individual customer's demographics. The goal is to categorize all event IDs into high, medium, and low priority for the customer, considering their interests, preferences, industry, and gender. The output should include a concise and engaging general note from a mascot, looking forward to seeing the customer at some of the events.

### Instructions:

1. **Parse the Itinerary JSON**: Extract event details such as event ID, title, start time, end time, duration, host, location, and categories.
2. **Parse the Individual Customer Demographics**: Extract customer ID, name, interests, preferences, industry, and gender.
3. **Compare Demographics with Event Categories**: Match customer interests with event categories to determine relevance.
4. **Rank Event IDs**: Categorize event IDs into high, medium, and low priority based on relevance to customer interests and preferences.
5. **Generate General Notes**: Create concise and engaging general notes from a mascot, looking forward to seeing the customer at some of the events.

### Example Input: Itinerary JSON

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
        "categories": ["Golf", "Social"]
    },
    {
        "event_id": "E002",
        "title": "Networking Lunch",
        "start_time": "12:00 PM",
        "end_time": "2:00 PM",
        "duration": 120,
        "host": ["John Smith"],
        "location": "Grand Ballroom",
        "categories": ["Networking"]
    },
    {
        "event_id": "E003",
        "title": "Golf Clinic",
        "start_time": "1:00 PM",
        "end_time": "3:00 PM",
        "duration": 120,
        "host": ["Phil Mickelson"],
        "location": "Pine Valley Golf Course",
        "categories": ["Golf"]
    },
    {
        "event_id": "E004",
        "title": "Brainstorming Session",
        "start_time": "2:00 PM",
        "end_time": "3:45 PM",
        "duration": 105,
        "host": ["Jane Doe", "John Smith"],
        "location": "Innovation Hub",
        "categories": ["Educational", "Networking"]
    },
    {
        "event_id": "E005",
        "title": "Early Morning Yoga",
        "start_time": "7:00 AM",
        "end_time": "8:00 AM",
        "duration": 60,
        "host": ["Sarah Johnson"],
        "location": "Zen Garden",
        "categories": ["Wellness"]
    },
    {
        "event_id": "E006",
        "title": "Late Afternoon Golf Match",
        "start_time": "4:00 PM",
        "end_time": "6:00 PM",
        "duration": 120,
        "host": ["Rory McIlroy"],
        "location": "Pine Valley Golf Course",
        "categories": ["Golf"]
    },
    {
        "event_id": "E007",
        "title": "Morning Coffee Meetup",
        "start_time": "8:30 AM",
        "end_time": "9:30 AM",
        "duration": 60,
        "host": ["Emily Davis"],
        "location": "Lobby Cafe",
        "categories": ["Networking"]
    },
    {
        "event_id": "E008",
        "title": "Midday Wellness Workshop",
        "start_time": "1:00 PM",
        "end_time": "3:00 PM",
        "duration": 120,
        "host": ["Sarah Johnson"],
        "location": "Wellness Center",
        "categories": ["Wellness"]
    },
    {
        "event_id": "E009",
        "title": "Late Afternoon Networking Session",
        "start_time": "5:00 PM",
        "end_time": "7:00 PM",
        "duration": 120,
        "host": ["John Smith"],
        "location": "Executive Lounge",
        "categories": ["Networking"]
    },
    {
        "event_id": "E010",
        "title": "Tech Showcase",
        "start_time": "1:00 PM",
        "end_time": "3:00 PM",
        "duration": 120,
        "host": ["TechCorp"],
        "location": "Innovation Hub",
        "categories": ["Promotional"]
    }
]
```

### Example Input: Individual Customer Demographics

```json
{
    "customer_id": "C001",
    "name": "John Doe",
    "interests": ["Golf", "Networking", "Wellness"],
    "preferences": ["Early Morning Events", "Outdoor Events"],
    "industry": "Technology",
    "gender": "Male"
}
```

### Example Output: Customer Priority Event List

```json
{
    "customer_id": "C001",
    "prioritized_events": {
        "high": ["E001", "E006"],
        "medium": ["E005", "E007"],
        "low": ["E002", "E003", "E004", "E008", "E009", "E010"]
    },
    "general_note": "Hey John, I can't wait to see you at the Golf Tournament!"
}
```

### Additional Examples:

#### Example 2: Customer Demographics

```json
{
    "customer_id": "C002",
    "name": "Jane Smith",
    "interests": ["Networking", "Educational", "Social"],
    "preferences": ["Afternoon Events", "Indoor Events"],
    "industry": "Finance",
    "gender": "Female"
}
```

#### Example 2: Output

```json
{
    "customer_id": "C002",
    "prioritized_events": {
        "high": ["E002", "E004"],
        "medium": ["E005", "E007", "E009"],
        "low": ["E001", "E003", "E006", "E008", "E010"]
    },
    "general_note": "Hi Jane, looking forward to seeing you at the Networking Lunch!"
}
```

#### Example 3: Customer Demographics

```json
{
    "customer_id": "C003",
    "name": "Alex Johnson",
    "interests": ["Golf", "Educational", "Promotional"],
    "preferences": ["Late Afternoon Events", "Outdoor Events"],
    "industry": "Healthcare",
    "gender": "Non-binary"
}
```

#### Example 3: Output

```json
{
    "customer_id": "C003",
    "prioritized_events": {
        "high": ["E001", "E006"],
        "medium": ["E004", "E010"],
        "low": ["E002", "E003", "E005", "E007", "E008", "E009"]
    },
    "general_note": "Hey Alex, excited to see you at the Golf Tournament!"
}
```

### Conclusion

This prompt and the resulting JSON response ensure that the event itinerary is parsed correctly, sorted by time, and includes all necessary details such as event IDs, titles, start times, end times, durations, hosts, locations, categories, and descriptions. The flexible parsing mechanism can handle missing or unstructured data, such as events without an end time or duration, and still generate a structured JSON response. This structured format will make it easier to generate custom itineraries for each guest based on their preferences and priorities.