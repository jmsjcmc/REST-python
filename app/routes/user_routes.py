from flask import Blueprint, request, jsonify
from app.services.user_service import users, user

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=["GET"])
def users():
    return jsonify(users())

@user_bp.route('/user', methods=["POST"])
def user():
    data = request.get_json()
    return user(data)