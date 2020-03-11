from flask import Blueprint, jsonify, request
# << Merge with the models for this to work, rename User and user to appropriate Model
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
            comment_data = {
                'id': comment.id,
                'text': comment.text,
                'user': comment.user,
                'thread': comment.thread,

            }

            result.append(comment_data)
        return jsonify(result), 200

    else:
        return jsonify({'message': 'id given does not match any thread_id'}), 400


@comments_api_blueprint.route('/new/<thread_id>', methods=['POST'])
def create(thread_id):
    comment = request.get_json()

    comment_text = comment.text
    comment_user = comment.user

    new_comment = Comment(
        text=comment_text, thread=thread_id, user=comment_user)
    if new_comment.save():
        return jsonify({
            'message': 'new comment created!',
            'status': 'success',
            'new_comment': {
                'id': new_comment.id,
                'user': new_comment.user,
                'text': new_comment.text,
                'thread': new_comment.thread,
            },
        }), 200
    else:
        return jsonify({'message': 'comment create failed'}), 400
