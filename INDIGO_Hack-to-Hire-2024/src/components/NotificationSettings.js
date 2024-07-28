import React, { useState, useEffect } from 'react';
import axios from 'axios';

const NotificationSettings = ({ userId }) => {
  const [notifications, setNotifications] = useState([]);

  useEffect(() => {
    axios.get(`/api/notifications/${userId}`)
      .then(response => setNotifications(response.data.notifications))
      .catch(error => console.error('Error fetching notifications:', error));
  }, [userId]);

  const handleSave = () => {
    axios.post(`/api/notifications/${userId}`, { notifications })
      .then(response => alert(response.data.success))
      .catch(error => console.error('Error updating notifications:', error));
  };

  return (
    <div>
      <h1>Notification Settings</h1>
      <textarea
        value={notifications.join('\n')}
        onChange={e => setNotifications(e.target.value.split('\n'))}
      />
      <button onClick={handleSave}>Save</button>
    </div>
  );
};

export default NotificationSettings;
