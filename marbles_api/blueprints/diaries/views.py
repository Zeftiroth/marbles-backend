from flask import Blueprint, jsonify, request
# << Merge with the models for this to work, rename User and user to appropriate Model
from models.user import User
from models.diary import Diary
from playhouse.shortcuts import model_to_dict
import peeweedbevolve
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename

from marbles_api.utils.s3_uploader import upload_file_to_s3
from flask_jwt_extended import jwt_required, get_jwt_identity
from operator import attrgetter
from PIL import Image, ImageOps
import tempfile
import os

diaries_api_blueprint = Blueprint('diaries_api',
                                  __name__,
                                  template_folder='templates')


# POST API to make a diary entry for a particular user

@diaries_api_blueprint.route('/', methods=['POST'])
@jwt_required
def create():

    user_id = get_jwt_identity()

    content = request.form.get('caption')

    if not user_id or not content:
        response = {
            'message': 'All field were not provided'
        }
        return jsonify(response), 400

    post_entry = request.get_json()

    post_entry = Diary(user_id=user_id,
                       content=content)

    post_entry.save()

    return jsonify({
        'message': 'diary entry made',
        'user': post_entry.user_id,
        'content': post_entry.content

    }), 200

# GET API to retrieve a user's diary entries


@diaries_api_blueprint.route('/<id>', methods=['GET'])
def show(id):

    diaries = Diary.select().where(Diary.user_id == id)

    diary_data = []
    for diary in diaries:
        diary = model_to_dict(diary)
        diary_data.append(diary)
    return jsonify(diary_data), 200
