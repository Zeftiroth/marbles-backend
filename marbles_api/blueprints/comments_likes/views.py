from flask import Blueprint, jsonify, request
from models.user import User
from models.comment import Comment
from models.comment_like import CommentLike
from playhouse.shortcuts import model_to_dict

comment_likes_api_blueprint = Blueprint('comment_likes_api',
                                        __name__,
                                        template_folder='templates')


@comment_likes_api_blueprint.route('/c_like/<id>', methods=['POST'])
def create(id):
    cur_com = Comment.get_or_none(Comment.id == id)
    if not cur_com:
        return jsonify({"msg": "error, com id wrong"}), 400

    else:
        comment_like = request.get_json()

        user_id = comment_like['user']
        comment_id = comment_like['comment']

        existing_like = CommentLike.get_or_none(
            (CommentLike.user == user_id) & (CommentLike.comment == comment_id))

        if existing_like:
            return jsonify({
                'message': "You've already liked this thread"
            })

        new_comment_like = CommentLike(user=user_id,
                                       comment=comment_id)

        new_comment_like.save()

        return jsonify({
            'message': "Comment liked successfully",

        }), 200


# @comment_likes_api_blueprint.route('/c_unlike/<id>', methods=['POST'])
# def delete(id):
#     cur_com = Comment.get_or_none(Comment.id == id)
#     if not cur_com:
#         return jsonify({"msg": "error, com id wrong"}), 400

#     else:
#         comment_unlike = request.get_json()
#         comment_id = comment_unlike['comment']
#         user_id = comment_unlike['user']
#         del_com = CommentLike.get_or_none(
#             CommentLike.user == user_id) & (CommentLike.comment == comment_id)
#         if not del_com:
#             return jsonify({"msg": "invalid com/user id"}), 400
#         else:

#             del_com.delete_instance(recursive=True)
#             return jsonify({
#                 'message': "comment_like deleted"
#             }), 200


@comment_likes_api_blueprint.route('/<id>', methods=["GET"])
def show(id):
    com_likes = CommentLike.select().where(CommentLike.comment == id)
    com_like_data = []
    for com_like in com_likes:
        com_like = model_to_dict(com_like)
        del com_like['user']
        del com_like['comment']['thread']
        del com_like['comment']['user']
        com_like_data.append(com_like)
    return jsonify({"msg": com_like_data}), 200
