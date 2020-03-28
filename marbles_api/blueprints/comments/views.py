from flask import Blueprint, jsonify, request
from models.user import User
from models.comment import Comment
from playhouse.shortcuts import model_to_dict

comments_api_blueprint = Blueprint('comments_api',
                                   __name__,
                                   template_folder='templates')


@comments_api_blueprint.route('/<thread_id>', methods=['GET'])
def index(thread_id):
    comments = Comment.select().where(Comment.thread == thread_id)
    result = []

    if comments:
        for comment in comments:
            comment = model_to_dict(comment)
            del comment['thread']['user']
            del comment['user']
            result.append(comment)
        return jsonify({"comments": result}), 200

    else:
        return jsonify({'message': 'id given does not match any thread_id'}), 400


@comments_api_blueprint.route('/new/<thread_id>', methods=['POST'])
def create(thread_id):
    comment = request.get_json()

    comment_text = comment["text"]
    comment_user = comment["user"]

    new_comment = Comment(
        text=comment_text, thread=thread_id, user=comment_user)
    if new_comment.save():
        return jsonify({
            'message': 'new comment created!',
            'status': 'success',
            
            'user': new_comment.user,
            'text': new_comment.text,
            'thread': new_comment.thread,
            
        }), 200
    else:
        return jsonify({'message': 'comment create failed'}), 400


@comments_api_blueprint.route('/update/<id>', methods=['POST'])
def update(id):

    comment = Comment.get_by_id(id)

    up_comment = request.get_json()

    comment.text = up_comment['text']

    if comment.save():
        return jsonify({
            'message': 'successfully updated comment',
            'status': 'success',

        }), 200
    else:

        return jsonify({"message": "update comment failed"}), 400


@comments_api_blueprint.route('/del/<id>', methods=['POST'])
def delete(id):

    comment = Comment.get_by_id(id)

    if comment.delete_instance(recursive=True):
        return jsonify({
            'message': "comment deleted"
        }), 200
    else:

        return jsonify({'message': "delete comment failed"}), 400
