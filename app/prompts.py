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

condensed = """
**Prompt:**

Analyze the raw text event itinerary and generate a structured plaintext response. Extract key information and generate appropriate categories for each event based on the context of the entire itinerary.

For each event, identify and extract:

1. **Event ID**: Unique identifier (e.g., E001, E002).
2. **Date**: Event date.
3. **Title**: Event title.
4. **Time**: Start and end time (if available).
5. **Duration**: Duration in minutes if possible.
6. **Host(s)**: Host(s) or speaker(s).
7. **Location**: Event location.
8. **Categories**: 2-4 relevant categories based on event details and context.
9. **Description**: Additional event details.

When generating categories, consider:
- Event type (e.g., presentation, workshop, social gathering)
- Subject matter (e.g., technology, business, arts)
- Target audience (e.g., professionals, students, general public)
- Format (e.g., interactive, lecture, networking)

Provide a brief analysis of the overall itinerary, highlighting key themes, target audience, and the general focus of the event series.

**Example Input:**

Future of Work Conference 2023

Day 1: October 10, 2023

9:00 AM - 10:30 AM: Opening Keynote - "Embracing AI in the Workplace"
Speaker: Dr. Emily Watson, Chief Innovation Officer at TechFuture Corp
Location: Grand Ballroom
Discover how AI is reshaping various industries and learn strategies to prepare your organization for the AI-driven future.

11:00 AM - 12:30 PM: Panel Discussion - "Remote Work: Challenges and Opportunities"
Moderator: James Chen
Panelists: Sarah Brown (HR Director), Mark Johnson (Remote Work Consultant), Lisa Zhang (Tech Startup Founder)
Location: Conference Room A
Explore the pros and cons of remote work and discuss best practices for managing distributed teams.

**Example Output:**

Event Analysis:

E001
Date: October 10, 2023
Title: Opening Keynote - "Embracing AI in the Workplace"
Time: 9:00 AM - 10:30 AM
Duration: 90 minutes
Host: Dr. Emily Watson
Location: Grand Ballroom
Categories: Keynote, Artificial Intelligence, Workplace Innovation, Future Trends
Description: Discover how AI is reshaping various industries and learn strategies to prepare your organization for the AI-driven future.

E002
Date: October 10, 2023
Title: Panel Discussion - "Remote Work: Challenges and Opportunities"
Time: 11:00 AM - 12:30 PM
Duration: 90 minutes
Hosts: James Chen (Moderator), Sarah Brown, Mark Johnson, Lisa Zhang
Location: Conference Room A
Categories: Panel Discussion, Remote Work, HR Management, Workplace Trends
Description: Explore the pros and cons of remote work and discuss best practices for managing distributed teams.

Overall Itinerary Analysis:
The Future of Work Conference 2023 focuses on emerging trends and challenges in the modern workplace. Key themes include:

1. Technology Integration: The role of AI and other technologies in shaping future work environments.
2. Remote and Hybrid Work Models: Exploring the shift towards flexible work arrangements and their implications.
3. Workplace Design: Adapting physical and virtual spaces to support new ways of working.
4. Networking and Collaboration: Emphasizing the importance of professional connections in evolving work landscapes.

The target audience appears to be business leaders, HR professionals, and individuals interested in workplace innovation. The conference combines various formats, including keynote speeches, panel discussions, interactive workshops, and networking events, to provide a comprehensive learning and networking experience.

The general focus is on preparing attendees for the future of work by addressing technological advancements, changing work models, and the need for adaptive strategies in organizational management.
"""
