from flask import Blueprint, jsonify, request
from models import Flight
import json
from kafka import KafkaProducer

flights_blueprint = Blueprint('flights', __name__)

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

@flights_blueprint.route('/', methods=['GET'])
def get_all_flights():
    flights = Flight.get_all_flights()
    return jsonify(flights)

@flights_blueprint.route('/<flight_id>', methods=['GET'])
def get_flight_by_id(flight_id):
    flight = Flight.get_flight_by_id(flight_id)
    if flight:
        return jsonify(flight)
    return jsonify({"error": "Flight not found"}), 404

@flights_blueprint.route('/<flight_id>', methods=['PUT'])
def update_flight(flight_id):
    data = request.json
    Flight.update_flight(flight_id, data)
    producer.send('flight_updates', {'flight_id': flight_id, 'status': data.get('status')})
    return jsonify({"success": "Flight updated"})
