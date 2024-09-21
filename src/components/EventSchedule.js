import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { ChevronDown, ChevronUp, MapPin, Users, Clock, InfoIcon, Calendar, ChevronLeft, ChevronRight } from 'lucide-react';
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
            Host: {event.host || 'N/A'}
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

const DaySchedule = ({ dayData }) => {
  const [expandedEvent, setExpandedEvent] = useState(null);

  const toggleExpand = (index) => {
    setExpandedEvent(expandedEvent === index ? null : index);
  };

  return (
    <div className="mb-8">
      {dayData.map((event, index) => (
        <EventCard
          key={event.event_id}
          event={event}
          isExpanded={expandedEvent === index}
          toggleExpand={() => toggleExpand(index)}
          isFirst={index === 0}
        />
      ))}
    </div>
  );
};

const EventSchedule = () => {
  const [showQRCode, setShowQRCode] = useState(false);
  const [sortedData, setSortedData] = useState([]);
  const [currentDayIndex, setCurrentDayIndex] = useState(0);

  useEffect(() => {
    const fetchEvents = async () => {
      try {
        const response = await axios.get('http://localhost:8000/events');
        const events = response.data.events;
        const groupedByDate = events.reduce((acc, event) => {
          const date = event.date;
          if (!acc[date]) {
            acc[date] = [];
          }
          acc[date].push(event);
          return acc;
        }, {});
        const sortedDates = Object.keys(groupedByDate).sort((a, b) => new Date(a) - new Date(b));
        const sortedEvents = sortedDates.map(date => {
          const events = groupedByDate[date].sort((a, b) => new Date('1970/01/01 ' + a.start_time) - new Date('1970/01/01 ' + b.start_time));
          return { date, events };
        });
        setSortedData(sortedEvents);
      } catch (error) {
        console.error("Error fetching events:", error);
      }
    };

    fetchEvents();
  }, []);

  const toggleQRCode = () => {
    setShowQRCode(!showQRCode);
  };

  const goToPreviousDay = () => {
    setCurrentDayIndex((prevIndex) => Math.max(0, prevIndex - 1));
  };

  const goToNextDay = () => {
    setCurrentDayIndex((prevIndex) => Math.min(sortedData.length - 1, prevIndex + 1));
  };

  return (
    <div className="max-w-7xl mx-auto bg-white p-4 font-sans">
      <div className="border-2 border-black p-4 bg-white shadow-lg">
        <div className="mb-4">
          <h1 className="text-2xl md:text-4xl font-bold mb-2 text-black">GOLFFEST 2023</h1>
          <p className="text-lg md:text-xl mb-4 text-gray-700">A Multi-Day Golf, Networking, and Fun Event</p>
        </div>

        <div className="flex flex-row space-x-4 mb-4">
          <div className="flex-1 border-2 border-black p-3">
            <div className="flex justify-center items-center cursor-pointer" onClick={toggleQRCode}>
              <QRCodeSVG value="https://example.com" size={80} />
            </div>
          </div>

          <div className="flex-1 border-2 border-black p-3">
            <p className="flex items-center mb-2 text-gray-800">
              <Calendar size={16} className="mr-2" /> {sortedData.length > 0 ? `${new Date(sortedData[0].date).toLocaleDateString()} - ${new Date(sortedData[sortedData.length - 1].date).toLocaleDateString()}` : 'Loading...'}
            </p>
            <p className="flex items-center text-gray-800">
              <MapPin size={16} className="mr-2" /> Pine Valley Golf Club
            </p>
          </div>
        </div>

        {/* Mini Navbar for Date Navigation */}
        <div className="flex justify-between items-center mb-4 border-2 border-black p-2">
          <button
            onClick={goToPreviousDay}
            disabled={currentDayIndex === 0}
            className="p-2 disabled:opacity-50"
          >
            <ChevronLeft size={24} />
          </button>
          <span className="font-bold text-xl">
            {sortedData[currentDayIndex] ? new Date(sortedData[currentDayIndex].date).toLocaleDateString('en-US', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }) : 'Loading...'}
          </span>
          <button
            onClick={goToNextDay}
            disabled={currentDayIndex === sortedData.length - 1}
            className="p-2 disabled:opacity-50"
          >
            <ChevronRight size={24} />
          </button>
        </div>

        <div className="border-t-2 border-black pt-4 mt-4">
          {sortedData[currentDayIndex] && (
            <DaySchedule dayData={sortedData[currentDayIndex].events} />
          )}
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