from models.base_model import BaseModel
import peewee as pw
from models.user import Users
from models.thread import Threads


class ThreadLikes(BaseModel):
    user = pw.ForeignKeyField(Users, backref="comment_likes")
    thread = pw.ForeignKeyField(Threads, backref="comment_likes")
