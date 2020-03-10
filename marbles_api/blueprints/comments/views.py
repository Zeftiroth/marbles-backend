from flask import Blueprint, jsonify, request
# << Merge with the models for this to work, rename User and user to appropriate Model
from models.user import User
from playhouse.shortcuts import model_to_dict

comments_api_blueprint = Blueprint('comments_api',
                                   __name__,
                                   template_folder='templates')


