from models.base_model import BaseModel
import peewee as pw
from models.user import Users
from models.comment import Comments


class CommentLikes(BaseModel):
    user = pw.ForeignKeyField(Users, backref="comment_likes")
    comment = pw.ForeignKeyField(Comments, backref="comment_likes")
