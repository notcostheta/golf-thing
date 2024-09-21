#!/usr/bin/env python
# coding: utf-8

# In[13]:


import os
from groq import Groq
from dotenv import load_dotenv
from typing import List, Optional
from prompts import base, content, condensed
from pydantic import BaseModel, Field, RootModel

load_dotenv()


# In[34]:


from pydantic import BaseModel
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


# In[15]:


client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)


# In[16]:


resp = client.chat.completions.create(
    model="llama-3.1-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": condensed,
        },
        {
            "role": "user",
            "content": content,
        },
    ],
    # response_format={"type": "json_object"},
    temperature=0,
    max_tokens=8000,
)


# In[17]:


print(resp)


# In[18]:


print(resp.choices[0].message.content)


# In[19]:


thing_content = resp.choices[0].message.content


# In[20]:


json_thing = client.chat.completions.create(
    model="llama-3.1-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": base,
        },
        {
            "role": "user",
            "content": thing_content,
        },
    ],
    response_format={"type": "json_object"},
    temperature=0,
    max_tokens=8000,
)


# In[21]:


print(json_thing.choices[0].message.content)


# In[25]:


import json


json_thing_content = json.loads(json_thing.choices[0].message.content)


# In[32]:


from pydantic import ValidationError


def validate_json(json_data):
    try:
        event_itinerary = EventItinerary.model_validate(json_data)
        print("Validation successful!")
        return event_itinerary
    except ValidationError as e:
        print("Validation failed!")
        print(e.json())
        return None


# In[35]:


validate_json(json_thing_content)


# In[ ]:
