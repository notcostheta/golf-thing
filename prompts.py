base = """
Parse the raw text event itinerary and generate a structured JSON response. Ensure the response is sorted by event start times. Handle missing data, multiple hosts, and events without end times.
Identify the following fields from the raw text:
Required fields:

- `event_id`: Unique identifier.
- `title`: Event title.
- `start_time`: Start time.
- `end_time`: End time (if available).
- `duration`: Duration in minutes (if available).
- `host`: Host(s) as a list.
- `location`: Event location.
- `categories`: Categorize the Event in some form based on the potential attendee's demographic interest.
- `description`: Event description.

Example Input:
Event 1: Golf Tournament, 9:00 AM - 12:00 PM, Hosted by Tiger Woods and Lee Trevino, Location: Pine Valley Golf Course
Categories: Golf, Social
Description: Join Tiger Woods and other golf enthusiasts for a thrilling golf tournament.

Event 2: Welcome to the Conference, 10:00 AM, Hosted by Conference Chair, Location: Main Hall
Duration: 15 minutes
Categories: Social, Educational
Description: Get ready to kick off the conference with a warm welcome from our esteemed chair.


Example Output:
[
    {
        "event_id": "E001",
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
        "title": "Welcome to the Conference",
        "start_time": "10:00 AM",
        "end_time": null,
        "duration": 15,
        "host": ["Conference Chair"],
        "location": "Main Hall",
        "categories": ["Social", "Educational"],
        "description": "Get ready to kick off the conference with a warm welcome from our esteemed chair."
    },
]

Strictly return only the json response.

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

cot = """
To parse the raw text event itinerary and generate a structured JSON response, follow these steps:

1. Read through the entire raw text input to get an overview of the events.

2. For each event:
   a. Identify the event title
   b. Extract the start time
   c. Look for an end time (if available)
   d. Calculate the duration in minutes (if possible)
   e. Identify the host(s) and create a list
   f. Extract the location
   g. Identify and list the categories
   h. Extract the description
   i. Generate a unique event_id (e.g., E001, E002, etc.)

3. Create a JSON object for each event with the following structure:
   {
     "event_id": "...",
     "title": "...",
     "start_time": "...",
     "end_time": "..." or null,
     "duration": ... or null,
     "host": [...],
     "location": "...",
     "categories": [...],
     "description": "..."
   }

4. Sort the events by start time.

5. Combine all event JSON objects into a single array.

6. Review the final JSON structure to ensure all required fields are present and formatted correctly.

7. Return only the JSON response, without any additional text or explanation.

Remember to handle missing data appropriately, such as using null for missing end times or durations. Ensure that hosts are always represented as a list, even if there's only one host. Categorize events according to the provided list (Golf, Networking, Wellness, Promotional, Panel, Social, Educational) based on the content and context of each event.
"""
