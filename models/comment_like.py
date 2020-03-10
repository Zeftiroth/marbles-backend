from models.base_model import BaseModel
import peewee as pw
from models.user import User
from models.comment import Comment


class CommentLike(BaseModel):
    user = pw.ForeignKeyField(User, backref="comment_likes")
    comment = pw.ForeignKeyField(Comment, backref="comment_likes")
