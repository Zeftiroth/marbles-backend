from app import app
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from marbles_api.blueprints.users.views import users_api_blueprint
from marbles_api.blueprints.emergencies.views import emergencies_api_blueprint
from marbles_api.blueprints.threads.views import threads_api_blueprint
from marbles_api.blueprints.comments.views import comments_api_blueprint
from marbles_api.blueprints.comments_likes.views import comment_likes_api_blueprint
from marbles_api.blueprints.sessions.views import sessions_api_blueprint

from marbles_api.blueprints.thread_likes.views import thread_likes_api_blueprint
from marbles_api.blueprints.diaries.views import diaries_api_blueprint

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

## API Routes ##


app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

app.register_blueprint(users_api_blueprint, url_prefix='/api/v1/users')

app.register_blueprint(emergencies_api_blueprint,
                       url_prefix='/api/v1/emergencies')

app.register_blueprint(threads_api_blueprint,
                       url_prefix='/api/v1/threads')

app.register_blueprint(comments_api_blueprint, url_prefix='/api/v1/comments')


app.register_blueprint(sessions_api_blueprint, url_prefix='/api/v1/sessions')

app.register_blueprint(comment_likes_api_blueprint,
                       url_prefix='/api/v1/comment_like')
app.register_blueprint(thread_likes_api_blueprint,
                       url_prefix='/api/v1/thread_likes')

app.register_blueprint(diaries_api_blueprint,
                       url_prefix='/api/v1/diaries')
