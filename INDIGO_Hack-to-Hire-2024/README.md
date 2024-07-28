# Flight Status and Notifications System

## Overview

This project provides real-time flight status updates and notifications to passengers. The system displays current flight status, sends notifications for changes, and integrates with airport databases for accurate information.

## Features

- Real-time flight status updates (delays, cancellations, gate changes).
- Push notifications via SMS, email, or app notifications.
- Integration with airport systems for accurate data.

## Technologies

- **Frontend**: HTML, CSS, React.js
- **Backend**: Python (Flask)
- **Database**: MongoDB
- **Notifications**: Kafka

## Setup Instructions

1. **Frontend**:
  
   cd frontend
   npm install
   npm start

Backend:
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py


Database: Set up MongoDB instance and configure the connection in config.py.

Kafka: Set up Kafka instance and configure producers/consumers in the backend.


Additional Tools and Libraries
Axios for API requests in the frontend.
WebSockets for real-time updates.
Bootstrap/Material-UI for styling.


### Expected Output

#### Frontend

1. **Flight Status Page**: Displays a list of flights with their current status, gate, etc.
2. **Notification Settings Page**: Allows users to configure their notification preferences.

#### Backend

1. **API Endpoints**:
   - `/api/flights/`: Fetches all flights.
   - `/api/flights/<flight_id>`: Fetches or updates a specific flight.
   - `/api/notifications/<user_id>`: Fetches or updates a user's notification preferences.

2. **Kafka Integration**:
   - Sends flight status updates to the `flight_updates` topic.

3. **MongoDB Integration**:
   - Stores flight data and user notification preferences.



#### json

**Backend API Responses**
#### Fetch All Flights (GET /api/flights/)
Response:


[
  {
    "_id": "60d9fbd6c045c8b2f8f6e4e9",
    "number": "123",
    "status": "On Time",
    "gate": "A1"
  },
  
  {
    "_id": "60d9fbd6c045c8b2f8f6e4ea",
    "number": "456",
    "status": "Delayed",
    "gate": "B2"
  },
  
  {
    "_id": "60d9fbd6c045c8b2f8f6e4eb",
    "number": "789",
    "status": "Cancelled",
    "gate": "C3"
  }
]

#### Fetch Single Flight (GET /api/flights/<flight_id>)
Response:


{
  "_id": "60d9fbd6c045c8b2f8f6e4e9",
  "number": "123",
  "status": "On Time",
  "gate": "A1"
}

#### Update Flight (PUT /api/flights/<flight_id>)
Request:


{
  "status": "Delayed",
  "gate": "A2"
}

Response:


{
  "success": "Flight updated"
}

#### Fetch User Notifications (GET /api/notifications/<user_id>)
Response:


{
  "_id": "userId123",
  "notifications": [
    "email@example.com",
    "+1234567890 (SMS)",
    "App notifications: Enabled"
  ]
}

#### Update User Notifications (POST /api/notifications/<user_id>)
Request:

{
  "notifications": [
    "email@example.com",
    "+1234567890 (SMS)",
    "App notifications: Enabled"
  ]
}

Response:


{
  "success": "Notifications updated"
}
