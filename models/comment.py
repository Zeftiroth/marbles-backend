from models.base_model import BaseModel
import peewee as pw
from models.user import User
from models.thread import Thread


class Comment(BaseModel):
    thread = pw.ForeignKeyField(Thread, backref="comments")
    user = pw.ForeignKeyField(User, backref="comments")
    text = pw.TextField(null=True)
