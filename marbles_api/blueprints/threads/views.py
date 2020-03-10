from flask import Blueprint, jsonify, request
# << Merge with the models for this to work, rename User and user to appropriate Model
from models.user import User
from models.thread import Thread
from playhouse.shortcuts import model_to_dict

threads_api_blueprint = Blueprint('threads_api',
                                  __name__,
                                  template_folder='templates')


# ------- API TO RETURN ALL THREADS ---------

@threads_api_blueprint.route('/', methods=["GET"])
def index():
    threads = Thread.select()
    thread_data = []
    for thread in threads:
        thread = model_to_dict(thread)
        thread_data.append(thread)
    return jsonify(thread_data), 200


# ------ API THAT SELECTS A THREAD BY ID -----------
@threads_api_blueprint.route('/<id>', methods=['GET'])
def show(id):
    thread = Thread.get_or_none(User.id == id)

    if thread:
        return jsonify({
            'id': thread.id,
            'template': thread.template,
            'content': thread.content
        }), 200
    else:
        return jsonify({'message': 'thread not found'}), 418

# ---------- API THAT CREATES A NEW THREAD, RETURNS A new_thread OBJECT BACK ---------
# @threads_api_blueprint.route('/', methods=['POST'])
# def create():


# Need to get the ID of the user creating the new thread.

# post_thread = request.get_json()

# user = User.get_or_none(User.id == post_thread.threads.id)

# new_thread = Thread(

# )
