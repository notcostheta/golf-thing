import React, { useState } from 'react';
import { ChevronDown, ChevronUp, MapPin, Users, Clock } from 'lucide-react';
import eventsData from '../data/events.json'; // Import the JSON file

const EventCard = ({ event, isExpanded, toggleExpand }) => {
  return (
    <div className="mb-4 border-2 border-black bg-white">
      <div 
        className="grid grid-cols-3 p-2 cursor-pointer hover:bg-gray-100 transition-colors duration-200"
        onClick={toggleExpand}
      >
        <div className="col-span-2">
          <div className="text-xs text-gray-600">Time</div>
          <div className="text-lg font-bold text-black">{event.time_slot}</div>
        </div>
        <div className="col-span-1 flex items-center justify-end">
          {isExpanded ? <ChevronUp size={24} className="text-black" /> : <ChevronDown size={24} className="text-black" />}
        </div>
      </div>
      <div className={`p-2 border-t-2 border-black ${isExpanded ? '' : 'hidden'}`}>
        <h3 className="text-lg font-bold mb-2 text-black">{event.event_name}</h3>
        <p className="flex items-center mb-1 text-gray-800"><MapPin size={16} className="mr-2" /> {event.location}</p>
        <p className="flex items-center mb-1 text-gray-800"><Clock size={16} className="mr-2" /> {event.time_slot}</p>
        <p className="flex items-center mb-1 text-gray-800"><Users size={16} className="mr-2" /> {event.category}</p>
        {event.priority && (
          <p className="text-sm text-gray-600">Priority: {event.priority}</p>
        )}
      </div>
    </div>
  );
};

const EventSchedule = () => {
  const [expandedEvent, setExpandedEvent] = useState(null);

  const toggleExpand = (index) => {
    setExpandedEvent(expandedEvent === index ? null : index);
  };

  return (
    <div className="max-w-7xl mx-auto bg-white p-4 font-sans">
      <div className="border-2 border-black p-4 bg-white shadow-lg">
        <div className="md:flex md:justify-between md:items-center">
          <div>
            <h1 className="text-2xl md:text-4xl font-bold mb-2 text-black">GOLFFEST 2023</h1>
            <p className="text-lg md:text-xl mb-4 text-gray-700">A Day of Golf, Networking, and Fun</p>
          </div>
          <div className="border-2 border-black p-3">
            <p className="flex items-center mb-2 text-gray-800">
              <Clock size={16} className="mr-2" /> June 15, 2023
            </p>
            <p className="flex items-center text-gray-800">
              <MapPin size={16} className="mr-2" /> Pine Valley Golf Club
            </p>
          </div>
        </div>
        <div className="border-t-2 border-black pt-4 md:grid md:grid-cols-2 md:gap-4 mt-4">
          {eventsData.map((event, index) => (
            <EventCard
              key={index}
              event={event}
              isExpanded={expandedEvent === index}
              toggleExpand={() => toggleExpand(index)}
            />
          ))}
        </div>
      </div>
    </div>
  );
};

export default EventSchedule;