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

content = """
             
ARMY  INSTITUTE OF  MANAGEMENT  & TECHNOLOGY  
                                    GREATER  NOIDA  
Armotsav 2K22 -Annual Cultural and Sports Fest  
 
27th April 2022 - Sports Itinerary   
Time  Event  Venue  
5:00-5:30 PM  March Past  Football Ground  
5:30-6:00 PM  100 m Heats Boys and 
Girls  Football Ground  
5:30-6:30 PM  Chess Boys and Girls  Amphitheatre  
6:15-7:00PM  Football (Match -1) Football Ground  
 
 
28th April 2022 - Sports Event Itinerary  
Time  Event  Venue  
7:00-8:00 AM  Basketball Boys (Match -1) Basketball court  
7:00-8:30 AM  Badminton Boys and Girls  Badminton court  
7:00-8:30 AM  Table Tennis Boys and Girls  Cafeteria  
8:00-9:00 AM  Football (Match -2) Football Court  
5:30-6:15 PM  Volleyball Boys (Match -1) Volleyball Court  
6:20-7:00PM  Volleyball Boys (Match -2) Volleyball Court  
 
 
28th April 2022 - Cultu ral Event Itinerary  
Time  Event  Venue  
10:00 -11:30 Hrs  Quiz  Seminar hall  
11:45-13:00 Hrs Solo Singing  Seminar hall  
13:00  -13:30 Hrs  Poem Recitation / 
Shayari / Stand Up   Seminar hall  
13:00 -14:30 Hrs  Lunch  
15:00 -16:15 Hrs Solo Dancing  Seminar hall  
16:15-16:30 Hrs Talent round  Seminar hall  
 
29th April 2022  - Sports Itinerary  
Time  Event  Venue  
7:00-8:00 AM  Basketball Boys 
(Match -2) Basketball Court  
7:00-8:30 AM  Badminton Boys 
and Girls Final  Badminton Court  
7:00-8:30 AM  Table Tennis Boys 
and Girls Finals  Cafeteria  
 8:00-9:00  AM  Basketball 
Girls(Finals)  Basketball Court  
4:00 -5:00 PM  Basketball 
Boys(Finals)  Basketball Court  
4:00-5:00 PM  Chess Bo ys and 
Girls (Final)  Amphitheatre  
5:00- 6:00 PM  Volleyball 
Girls(Finals)  Volleyball Court  
 6:00 – 7:00 PM  Volleyball 
Boys(Finals)  Volleyball Court  
  
29th April 2022  – Cultural Itinerary  
10:00 -11:30 Hrs  Group singing  Seminar Hall  
11:45-12:25 Hrs  Rap battle  
/Photography/ E -
Posters /  Video 
Pitching  Seminar hall  
12:30 -13:30 Hrs  Nukkad natak  Seminar Hall  
13:00 -14:30 Hrs  Lunch  
14:45 -16:00 Hrs Group Dance   Seminar Hall  
 
 
30th April 2022  – Sports  Itinerary  
Time  Event  Venue  
7:00-7:20 AM  100m Boys Final  Football Ground  
7:25-7:45 AM  100m Girls Final  Football Ground  
7:50-9:00 AM  Football (Finals )  Football Ground  
 
 
 
 
 
 
 
 
 30th April 2022  – Culmination  Day 
Time  Event  Venue  
11:00 Hrs – 13:00 Hrs   Fashion  Show -
Prelims   Seminar hall  
13:00 Hrs – 14:30 Hrs  Lunch  
16:25 -16:30 Hrs  Arrival of Chief 
Guest  and 
preliminaries  
 To be Received by 
Director AIMT, Fest 
coordinator, and 
students  
16:30 -1635 Hrs  Welcome address 
by Director, AIMT  
 Seminar hall  
16:35-16:55 Hrs  Fashion Show 
Finals  Seminar hall  
17:00Hrs – 17:30 Hrs  Cultural Program  Seminar hall  
17:30 Hrs to 17:55 Hrs  Prize Distribution  Seminar hall  
17:55 Hrs – 18:05 Hrs Chief Guest’s 
Address     
 Seminar hall  
18:05  Hrs – 18:10 Hrs  Vote of Thanks 
followed by 
National Anthem  
 Seminar hall  
18:10 Hrs -18:30 Hrs  High Tea  Cafeteria  
"""
