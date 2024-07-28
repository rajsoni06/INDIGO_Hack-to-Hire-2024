import React from 'react';
import FlightStatus from './FlightStatus';
import NotificationSettings from './NotificationSettings';

const FlightList = ({ userId }) => (
  <div>
    <FlightStatus />
    <NotificationSettings userId={userId} />
  </div>
);

export default FlightList;
