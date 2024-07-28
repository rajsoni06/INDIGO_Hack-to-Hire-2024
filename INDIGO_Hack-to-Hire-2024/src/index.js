import React, { useEffect, useState } from 'react';
import axios from 'axios';

const FlightStatus = () => {
  const [flights, setFlights] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/api/flights/')
      .then(response => setFlights(response.data))
      .catch(error => console.error('Error fetching flight data:', error));
  }, []);

  return (
    <div>
      <h1>Flight Status</h1>
      <ul>
        {flights.map(flight => (
          <li key={flight._id}>
            Flight {flight.number} - Status: {flight.status} - Gate: {flight.gate}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default FlightStatus;
