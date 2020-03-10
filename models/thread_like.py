from models.base_model import BaseModel
import peewee as pw
from models.user import User
from models.thread import Thread


class ThreadLike(BaseModel):
    user = pw.ForeignKeyField(User, backref="thread_likes")
    thread = pw.ForeignKeyField(Thread, backref="thread_likes")
