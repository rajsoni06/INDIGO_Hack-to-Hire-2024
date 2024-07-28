import React from 'react';
import FlightList from './components/FlightList';

const App = () => {
  const userId = 'sampleUserId'; // Replace with actual user ID logic
  return (
    <div>
      <h1>Flight Status and Notifications</h1>
      <FlightList userId={userId} />
    </div>
  );
};

export default App;
