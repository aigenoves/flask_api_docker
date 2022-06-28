from flask import Blueprint, request, jsonify
import json

classification_api = Blueprint('classification_api', __name__)

@classification_api.route("/classification")
def classification():
    sample = json.loads(request.data)["text"]
    return jsonify(sample)
