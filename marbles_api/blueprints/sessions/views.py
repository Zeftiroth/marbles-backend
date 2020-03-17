from flask import Blueprint, jsonify, request
from models.user import User
from werkzeug.security import check_password_hash


sessions_api_blueprint = Blueprint('sessions_api',
                                   __name__,
                                   template_folder='templates')


@sessions_api_blueprint.route('/login', methods=['POST'])
def login():
    login = request.get_json()
    print(login)
    user = User.get_or_none(User.name == login['name'])
    if user != None:
        result = User.get_or_none(User.password == login['password'])
        if result:

            return jsonify({'message': 'logged in successful'}), 200
        else:
            return jsonify({
                'message': 'incorrect password'

            }), 400
    else:
        return jsonify({'message': 'incorrect username and password'}), 400


# @sessions_api_blueprint.route('/logout')
# def logout():
#     logout_user()
#     print('message : logout succesful')
#     return jsonify({'msg': 'logout successful'}), 200
