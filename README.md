# Flight Status and Notifications System

## Description
This project provides a system to display real-time flight status updates and send notifications to passengers. The system is built using React.js for the frontend, Flask (Python) for the backend, PostgreSQL for the database, and RabbitMQ for the notification system.

## Tech Stack
- **Frontend**: React.js
- **Backend**: Flask (Python)
- **Database**: PostgreSQL
- **Notifications**: RabbitMQ

## How to Run

### Frontend
1. Navigate to the `flight-status-app` directory.
2. Run `npm install` to install dependencies.
3. Run `npm start` to start the React application.

### Backend
1. Run `pip install Flask Flask-Cors psycopg2-binary pika` to install dependencies.
2. Run `python app.py` to start the Flask server.

### Database
1. Set up PostgreSQL and create the database.
2. Run the SQL commands in `Schema.sql` to create the schema and insert initial data.

### Notifications
1. Run `python consumer.py` to start the RabbitMQ consumer.

## Additional Tools and Libraries
- Axios for HTTP requests in React.
- Flask-CORS for handling Cross-Origin Resource Sharing.
