from flask import Flask
from routes.flights import flights_blueprint
from routes.notifications import notifications_blueprint
from config import Config
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.from_object(Config)

mongo = PyMongo(app)

app.register_blueprint(flights_blueprint, url_prefix='/api/flights')
app.register_blueprint(notifications_blueprint, url_prefix='/api/notifications')

if __name__ == '__main__':
    app.run(debug=True)
