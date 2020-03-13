from flask import Blueprint, jsonify, request
# << Merge with the models for this to work, rename User and user to appropriate Model
from models.user import User
from models.thread import Thread
from playhouse.shortcuts import model_to_dict
import peeweedbevolve
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from flask_login import current_user, login_required
from marbles_api.utils.s3_uploader import upload_file_to_s3
from operator import attrgetter
from PIL import Image, ImageOps
import tempfile
import os


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
@threads_api_blueprint.route('/', methods=['POST'])
# @jwt_required
def create():

    # in future can use get_jwt_identity as a current_user
    # user_id = get_jwt_identity() < can use this to assign the user_id

    # Need to get the ID of the user creating the new thread.

    user_id = request.json.get('user')
    template = request.json.get('template')
    content = request.json.get('content')

    if not user_id or not template or not content:
        response = {
            'message': 'All field were not provided'
        }

        return jsonify(response), 400
    post_thread = request.get_json()

    post_thread = Thread(user_id=user_id,
                         template=template, content=content)

    post_thread.save()

    return jsonify({
        'message': 'thread made',
        'user': post_thread.user_id,
        'template': post_thread.template,
        'content': post_thread.content

    }), 200

# ---------API FOR USER TO EDIT THREAD -----------
@threads_api_blueprint.route('/<id>', methods=['POST'])
def update(id):

    thread = Thread.get_by_id(id)

    new_thread = request.get_json()

    thread.template = new_thread['template']
    thread.content = new_thread['content']

    if thread.save():
        return jsonify({
            'message': 'successfully updated thread',
            'status': 'success',
            'updated_thread': {
                'id': thread.id,
                'template': thread.template,
                'content': thread.content,
            },
        }), 200
    else:
        er_msg = []
        for error in thread.errors:
            er_msg.append(error)
        return jsonify({'message': er_msg}), 418

# --------API FOR DELETING THREAD --------------
@threads_api_blueprint.route('/<id>/delete', methods=['POST'])
def destroy(id):

    thread = Thread.get_by_id(id)

    if thread.delete_instance(recursive=True):
        return jsonify({
            'message': "thread deleted"
        }), 200
    else:
        er_msg = []
        for error in thread.errors:
            er_msg.append(error)
        return jsonify({'message': er_msg}), 418


@threads_api_blueprint.route("/upload/<thread_id>", methods=["POST"])
def upload(thread_id):
    if not 'image' in request.files:

        return jsonify({'msg': 'no image given'}), 400

    file = request.files.get('image')

    new_image = Image.open(file)

    resized_image = ImageOps.fit(
        new_image, (500, 500), method=3, bleed=0.0, centering=(0.5, 0.5))

    temp_storage = f"./marbles_api/static/temp/{file.filename}"

    resized_image.save(temp_storage)

    file.filename = secure_filename(file.filename)
    breakpoint()

    if not upload_file_to_s3(temp_storage, file):
        return jsonify({'msg': 'upload to s3 failed'}), 400

    thread = Thread.get_or_none(Thread.id == thread_id)
    thread.template = file.filename
    thread.save()

    os.remove(temp_storage)

    return jsonify({'msg': 'upload to s3 success'}), 200
