from flask import Blueprint, request, jsonify
from models import User

notifications_blueprint = Blueprint('notifications', __name__)

@notifications_blueprint.route('/<user_id>', methods=['GET'])
def get_user_notifications(user_id):
    notifications = User.get_user_notifications(user_id)
    if notifications:
        return jsonify(notifications)
    return jsonify({"error": "User not found"}), 404

@notifications_blueprint.route('/<user_id>', methods=['POST'])
def update_user_notifications(user_id):
    notifications = request.json.get('notifications')
    if notifications:
        User.update_user_notifications(user_id, notifications)
        return jsonify({"success": "Notifications updated"})
    return jsonify({"error": "Invalid data"}), 400
