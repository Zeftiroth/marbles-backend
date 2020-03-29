from flask import Blueprint, jsonify, request
# << Merge with the models for this to work, rename User and user to appropriate Model
from models.user import User
from models.thread_like import ThreadLike
from playhouse.shortcuts import model_to_dict

thread_likes_api_blueprint = Blueprint('thread_likes_api',
                                       __name__,
                                       template_folder='templates')

# Other users can like a thread. can retrieve number of likes

# ------- API TO CREATE A LIKE FOR A THREAD ----------

# create a thread_like
@thread_likes_api_blueprint.route('/', methods=['POST'])
def create():
    user_id = request.json.get('user_id')
    thread_id = request.json.get('thread_id')

    # VALIDATION. If the user has already liked the thread, throw up an error
    existing_like = ThreadLike.get_or_none(
        (ThreadLike.user == user_id) & (ThreadLike.thread == thread_id))

    if existing_like:
        return jsonify({
            'message': "You've already liked this thread"
        })

    new_thread_like = ThreadLike(user=user_id,
                                 thread=thread_id)

    new_thread_like.save()

    return jsonify({
        'message': "This tread was liked",
        "id": new_thread_like.id,
        "user": new_thread_like.user.name,
        "thread": new_thread_like.thread_id
    }), 200


# ----- API TO RETRIEVE ALL THE LIKES FOR A PARTICULAR THREAD BY ID ----
    # show number of likes for a thread
@thread_likes_api_blueprint.route('/<id>', methods=["GET"])
def show(id):
    t_likes = ThreadLike.select().where(ThreadLike.thread == id)
    tl_data = []
    for t_like in t_likes:
        t_like = model_to_dict(t_like)
        del t_like['thread']['user']
        tl_data.append(t_like)
    return jsonify({"msg": tl_data}), 200
