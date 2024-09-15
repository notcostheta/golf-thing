import React, { useState, useEffect } from 'react';
import { ChevronDown, ChevronUp, MapPin, Users, Clock, InfoIcon } from 'lucide-react';
import eventsData from '../data/events.json';
import { QRCodeSVG } from 'qrcode.react';

const EventCard = ({ event, isExpanded, toggleExpand, isFirst }) => {
  return (
    <div className="mb-4 flex">
      <div className="w-1/4 border-2 border-black bg-white mr-2">
        <div className="h-full flex flex-col justify-center items-center p-2">
          <div className={`text-xs text-gray-600 ${!isFirst ? 'hidden' : ''}`}>Start Time</div>
          <div className="text-lg font-bold text-black">{event.start_time}</div>
        </div>
      </div>
      <div className="w-3/4 border-2 border-black bg-white">
        <div 
          className="p-2 cursor-pointer hover:bg-gray-100 transition-colors duration-200"
          onClick={toggleExpand}
        >
          <div className="flex justify-between items-center">
            <div>
              <div className={`text-xs text-gray-600 ${!isFirst ? 'hidden' : ''}`}>Event</div>
              <div className="text-lg font-bold text-black">{event.title}</div>
            </div>
            {isExpanded ? <ChevronUp size={24} className="text-black" /> : <ChevronDown size={24} className="text-black" />}
          </div>
        </div>
        <div className={`p-2 border-t-2 border-black ${isExpanded ? '' : 'hidden'}`}>
          <p className="flex items-center mb-1 text-gray-800">
            <Clock size={16} className="mr-2" /> 
            {event.start_time} - {event.end_time} ({event.duration} min)
          </p>
          <p className="flex items-center mb-1 text-gray-800">
            <Users size={16} className="mr-2" /> 
            Host: {Array.isArray(event.host) ? event.host.join(', ') : event.host}
          </p>
          <p className="flex items-center mb-1 text-gray-800">
            <MapPin size={16} className="mr-2" /> 
            Location: {event.location}
          </p>
          {event.description && (
            <p className="flex items-start mt-2 text-gray-800">
              <InfoIcon size={16} className="mr-2 mt-1 flex-shrink-0" /> 
              <span>{event.description}</span>
            </p>
          )}
        </div>
      </div>
    </div>
  );
};

const EventSchedule = () => {
  const [expandedEvent, setExpandedEvent] = useState(null);
  const [showQRCode, setShowQRCode] = useState(false);
  const [sortedEvents, setSortedEvents] = useState([]);

  useEffect(() => {
    // Sort events by start_time
    const sorted = [...eventsData].sort((a, b) => {
      return new Date('1970/01/01 ' + a.start_time) - new Date('1970/01/01 ' + b.start_time);
    });
    setSortedEvents(sorted);
  }, []);

  const toggleExpand = (index) => {
    setExpandedEvent(expandedEvent === index ? null : index);
  };

  const toggleQRCode = () => {
    setShowQRCode(!showQRCode);
  };

  return (
    <div className="max-w-7xl mx-auto bg-white p-4 font-sans">
      <div className="border-2 border-black p-4 bg-white shadow-lg">
        <div className="mb-4">
          <h1 className="text-2xl md:text-4xl font-bold mb-2 text-black">GOLFFEST 2023</h1>
          <p className="text-lg md:text-xl mb-4 text-gray-700">A Day of Golf, Networking, and Fun</p>
        </div>
        
        <div className="flex flex-row space-x-4 mb-4">
          <div className="flex-1 border-2 border-black p-3">
            <div className="flex justify-center items-center cursor-pointer" onClick={toggleQRCode}>
              <QRCodeSVG value="https://example.com" size={80} />
            </div>
          </div>
          
          <div className="flex-1 border-2 border-black p-3">
            <p className="flex items-center mb-2 text-gray-800">
              <Clock size={16} className="mr-2" /> June 15, 2023
            </p>
            <p className="flex items-center text-gray-800">
              <MapPin size={16} className="mr-2" /> Pine Valley Golf Club
            </p>
          </div>
        </div>
        
        <div className="border-t-2 border-black pt-4 mt-4">
          {sortedEvents.map((event, index) => (
            <EventCard
              key={event.event_id}
              event={event}
              isExpanded={expandedEvent === index}
              toggleExpand={() => toggleExpand(index)}
              isFirst={index === 0}
            />
          ))}
        </div>
      </div>
      {showQRCode && (
        <div 
          className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50"
          onClick={toggleQRCode}
        >
          <div className="bg-white p-4 rounded-lg shadow-lg">
            <QRCodeSVG value="https://example.com" size={350} />
          </div>
        </div>
      )}
    </div>
  );
};

export default EventSchedule;