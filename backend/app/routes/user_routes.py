from flask import Blueprint, jsonify

bp = Blueprint('example', __name__)

@bp.route('/example', methods=['GET'])
def example():
    return jsonify({"message": "Hello, PostgreSQL!"})