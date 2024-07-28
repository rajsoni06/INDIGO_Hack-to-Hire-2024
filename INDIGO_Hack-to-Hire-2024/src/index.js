import React from 'react';
import FlightStatus from './components/FlightStatus';
import NotificationSettings from './components/NotificationSettings';

const App = () => {
  return (
    <div className="App">
      <FlightStatus />
      <NotificationSettings userId="userId123" />
    </div>
  );
};

export default App;
